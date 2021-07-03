<template>
  <div class="home">
    <h1 class="px-15 py-5 subheading teal--text text--darken-3">Home</h1>

    <v-container fluid class="mx-13">

      <v-layout row justify-start class="mb-3 px-10">
        <v-btn small flat outline dark class="teal lighten-1" @click="sortBy('sequence_number')">
          <v-icon small left>format_list_numbered</v-icon>
          <span class="caption">By Sequence Number</span>
        </v-btn>
        <v-btn small flat outline dark class="teal lighten-1" @click="sortBy('duration')">
          <v-icon small left>timelapse</v-icon>
          <span class="caption">By Duration</span>
        </v-btn>
      </v-layout>

      <v-card flat class="pa-4" outlined color="#CCFFCC" max-width="1300" v-for="record in records" :key="record.id">
        <v-layout row wrap :class="`pa-3 record ${record.status}`">
          <v-flex xs4 md2>
            <div class="caption teal--text text--darken-4">Sequence Number</div>
            <div>{{ record.sequence_number }}</div>
          </v-flex>
          <v-flex xs8 sm6 md3>
            <div class="caption teal--text text--darken-4">Start time</div>
            <div>{{ record.start_time_1 }}-{{ record.start_time_2 }}-{{ record.start_time_3 }} {{ record.start_time_4 }}:{{ record.start_time_5 }}:{{ record.start_time_6 }}</div>
          </v-flex>
          <v-flex xs8 sm6 md3>
            <div class="caption teal--text text--darken-4">End time</div>
            <div>{{ record.end_time_1 }}-{{ record.end_time_2 }}-{{ record.end_time_3 }} {{ record.end_time_4 }}:{{ record.end_time_5 }}:{{ record.end_time_6 }}</div>
          </v-flex>
          <v-flex xs8 sm6 md2>
            <div class="caption teal--text text--darken-4">Duration</div>
            <div>{{ record.duration_1 }} h {{ record.duration_2 }} m {{ record.duration_3 }} s </div>
          </v-flex>
          <v-flex xs8 sm6 md2>

            <div v-if="record.status === 'free'">
                <v-row justify="center my-2">
                  <v-dialog
                    v-model="dialog"
                    persistent
                    max-width="300"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                        color="teal lighten-1"
                        dark
                        v-bind="attrs"
                        v-on="on"
                        width="150"
                        @click.stop="dialog = true"
                        :retain-focus="false"
                      >
                        FREE
                      </v-btn>
                    </template>
                    <v-card>
                      <v-img
                        height="250"
                        src="/free.jpg"
                      ></v-img>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <div class="mx-13">
                          <v-btn
                            color="green"
                            outlined
                            @click="dialog = false"
                            width="170"
                          >
                            FREE!
                          </v-btn>
                        </div>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-row>
            </div>

            <div v-else>
                <v-row justify="center my-2">
                  <v-dialog
                    v-model="dialog2"
                    persistent
                    max-width="300"
                    :retain-focus="false"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                        color="teal lighten-1"
                        dark
                        v-bind="attrs"
                        v-on="on"
                        width="150"
                      >
                        occupied
                      </v-btn>
                    </template>
                    <v-card>
                      <v-img
                        height="250"
                        src="/occupied.jpg"
                      ></v-img>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <div class="mx-13">
                          <v-btn
                            color="red"
                            outlined
                            @click="dialog2 = false"
                            width="170"
                          >
                            OCCUPIED!
                          </v-btn>
                        </div>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-row>
            </div>

          </v-flex>

        </v-layout>
      </v-card>

    </v-container>

  </div>
</template>

<script>
import db from '@/fb'
export default {
  data() {
    return {
      dialog: false,
      dialog2: false,
      records: [
      ]
    }
  },
  methods: {
    sortBy(prop) {
      this.records.sort((a,b) => a[prop] < b[prop] ? -1 : 1)
    }
  },
  created() {
    db.collection('monitor').onSnapshot(res =>{
      const changes = res.docChanges();

      changes.forEach(change => {
        if (change.type === 'added'){
          this.records.push({
            id: change.doc.id,
            ...change.doc.data(),
          })
        }
        if (change.type === 'modified'){
          this.records.pop({
            id: change.doc.id,
            ...change.doc.data(),
          })
          this.records.push({
            id: change.doc.id,
            ...change.doc.data(),
          })          
        }        
      });
    })
  }
}
</script>

<style>

.record.occupied_person {
  border-left: 8px solid #FF6666;
  border-right: 8px solid #FF6666;
}
.record.occupied_belongings {
  border-left: 8px solid #FFFF99;
  border-right: 8px solid #FFFF99;
}
.record.free {
  border-left: 8px solid #3399CC;
  border-right: 8px solid #3399CC;
}
.record.occupied {
  border-left: 8px solid #FF6666;
  border-right: 8px solid #FF6666;
}
</style>