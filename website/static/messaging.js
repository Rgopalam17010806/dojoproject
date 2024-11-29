
const firebaseConfig = {
    apiKey: "AIzaSyCZWJH5JFipBh-_rr0khrhCKBvWxmD6it4",
    authDomain: "coderdojo-95920.firebaseapp.com",
    projectId: "coderdojo-95920",
    storageBucket: "coderdojo-95920.firebasestorage.app",
    messagingSenderId: "854705003277",
    appId: "1:854705003277:web:8044b96b74aead292f6e44",
    measurementId: "G-2SQ7NRV864"
  };

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const messaging = firebase.messaging();

// script.js

document.addEventListener('DOMContentLoaded', (event) => {
    // Check if notifications are supported by the browser
    if ('Notification' in window) {
        const notificationButton = document.getElementById('notificationButton');
        // Add click event listener to the button
        notificationButton.addEventListener('click', async () => {
            let permission = await Notification.requestPermission();
            if (permission === 'granted') {
                new Notification('Notifications enabled!');
            } else if(Notification.permission === 'denied') {
                alert("Notifications are denied. Please enable on the browser by clicking on the 'site information' on the address bar.");
            }
        });
        if (Notification.permission === 'granted') {
            messaging.getToken().then(function(token) {
                console.log(token);
                send_token(token);
            });
        }
    }
});

function send_token(token) {
    const url = window.location.origin + "/save_token";
    const data = {
        'user_id': user_id,
        'token': token
    };
    console.log(data);
    fetch(url, {
      method: 'POST', // Use the POST method
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json', // Set the content type to JSON
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
        console.log('Success:', data); // Handle the response data
    })
    .catch(error => {
      console.error('Error:', error); // Handle any errors
    });
}