<template>

  <nav>
    <!-- <v-toolbar dark app color="primary">

      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title class="text-uppercase">
        <span class="font-weight-light">Nap</span>
        <span>Ball</span>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn outlined>
        <span>Settings</span>
        <v-icon right>settings</v-icon>
      </v-btn>
    </v-toolbar> -->


      <v-navigation-drawer
        permanent
        expand-on-hover
        app
        dark
        class="teal lighten-1"
      >
        <v-list>
          <v-list-item class="px-2">
            <v-layout column >
              <v-flex class="">
                <v-avatar size="40">
                  <img src="/napball2.jpeg" alt="">
                </v-avatar>
              </v-flex>
            </v-layout>
            <v-list-item-avatar>
            </v-list-item-avatar>
          </v-list-item>

          <v-list-item link>
            <v-list-item-content>
              <v-list-item-title class="title text-uppercase">
                <span class="font-weight-light">Nap</span>
                <span>Ball</span>
              </v-list-item-title>
              <v-list-item-subtitle>NapBall@cuhk.edu.cn</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list
          nav
          dense
        >
          <v-list-item router-link to="/">
            <v-list-item-icon>
              <v-icon>weekend</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>
          <v-list-item router-link to="/about">
            <v-list-item-icon>
              <v-icon>leaderboard</v-icon>
            </v-list-item-icon>
            <v-list-item-title>About</v-list-item-title>
          </v-list-item>
          <v-list-item router-link to="/settings">
            <v-list-item-icon>
              <v-icon>settings</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Settings</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

    <!-- <v-navigation-drawer app v-model="drawer" class="primary">
      <p>test</p>
    </v-navigation-drawer> -->
  </nav>


</template>

<script>
export default {
  data() {
    return {
      drawer: false,
    }
  }
};
</script>
