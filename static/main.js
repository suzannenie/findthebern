'use strict';

//'https://findthebern.herokuapp.com/:8080'
var socket = io.connect('https://findthebern.herokuapp.com/:8080');
let name;
let points;
var level = 0;

socket.on('connect', function() {
    console.log("connected")
});

socket.on('your_score', function(data) {
    document.getElementById("your_score").innerHTML = data;
});

socket.on('leaderboard', function(data) {
    console.log('leaderboard');
    document.getElementById("leaderboard").innerHTML = data;
});

socket.on('current_round', function(data) {
    console.log('current round', data);
    level = data;
    getLevel();
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



function getLevel() {
  var i;
  var x = document.getElementsByClassName("levels");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[level].style.display = "";
}


function gameplay() {
    console.log("gamePlay");
}

$(".found").on("click", function(e){
    e.preventDefault();
    socket.emit('won_round', name);
});
