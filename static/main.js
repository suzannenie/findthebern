'use strict';

var socket = io();
let name;
let points;

socket.on('connect', function() {
    console.log("connected")
});

socket.on('leaderboard', function(data) {
    console.log('leaderboard');
    document.getElementById("leaderboard").innerHTML = data;
});


function toFind () {
    console.log("to find");
    name = document.getElementById("name_input").value
    if ( name.trim() == '' ) {
        document.getElementById("empty").style.display = "";
        return;
    }
    else {
        socket.emit('join_game', name);
        document.getElementById("home").style.display = "none";
        document.getElementById("game").style.display = "";
    }
}