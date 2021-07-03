import firebase from 'firebase/app'
import 'firebase/firestore'

var firebaseConfig = {
    apiKey: "AIzaSyCnswHqqrQ7KvAcRxFsu1X1bfMcb9OHuGo",
    authDomain: "exalted-skein-310719.firebaseapp.com",
    projectId: "exalted-skein-310719",
    storageBucket: "exalted-skein-310719.appspot.com",
    messagingSenderId: "369358608453",
    appId: "1:369358608453:web:56a9963389f4c6bc75eb2c",
    measurementId: "G-43441RCP4N"
  };
  // Initialize Firebase
firebase.initializeApp(firebaseConfig);

const db = firebase.firestore();

db.settings({ timestampsInSnapshots: true });

export default db;