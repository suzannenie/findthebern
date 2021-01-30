'use strict';

var socket = io();
let name;

function toFind () {
    console.log("to find");
    name = document.getElementById("name_input").value
    if ( name.trim() == '' ) {
        document.getElementById("empty").style.display = "";
        return;
    }
    else {
        console.log("here");
        socket.emit('join_game', name);;
    }
}

socket.on('connect', function() {
    console.log("connected")
});