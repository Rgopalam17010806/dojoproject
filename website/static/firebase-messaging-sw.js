importScripts('https://www.gstatic.com/firebasejs/3.6.8/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.6.8/firebase-messaging.js');

// Initialize Firebase
var config = {
   apiKey: "AIzaSyAW6b2CuYz_04hNb0GpWUS9wGoGsdHILI8",
   authDomain: "starlinglearn-2.firebaseapp.com",
   projectId: "starlinglearn-2",
   storageBucket: "starlinglearn-2.appspot.com",
   messagingSenderId: "704481200112",
   appId: "1:704481200112:web:59ffd10b2fe800da8fbf35"
};


firebase.initializeApp(config);
const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(payload => {
  console.log('[worker] Received push notification: ', payload);
  return self.registration.showNotification(payload.title, payload);
});