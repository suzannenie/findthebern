'use strict';

//'https://findthebern.herokuapp.com/:8080'
var socket = io.connect();
let name;
let points;
var level = 0;
var solo_round = 0;
let startTime;
let elapsedTime;
let timerInterval;

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

socket.on('update_solos', function(data) {
    document.getElementById("top_three").innerHTML = "<h5>Top Three Time Trials</h5>" + data;
    document.getElementById("top_three2").innerHTML = "<h5>Top Three </h5><br>" + data;
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


$(".found").on("click", function(e){
    e.preventDefault();
    socket.emit('won_round', name);
});



function toSolo () {
    name = document.getElementById("name_input").value
    if ( name.trim() == '' ) {
        document.getElementById("empty").style.display = "";
        return;
    }
    else {
        document.getElementById("home").style.display = "none";
        document.getElementById("solo").style.display = "";
        getSoloRound();
    }
}

$(".found_solo").on("click", function(e){
    e.preventDefault();
    getSoloRound();
});

function getSoloRound() {
  if (solo_round == 0) {
    startTimer();
  }
  var i;
  var x = document.getElementsByClassName("solos");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  if (solo_round == 5) {
    socket.emit('finish_solo', name, timeToString(elapsedTime));
    pause();
    document.getElementById("solo_game").style.display = "none";
    document.getElementById("solo_done").style.display = "";
    solo_round = 0;
  }
  x[solo_round].style.display = "";
  solo_round = solo_round + 1;
}

function startTimer(){
    startTime = Date.now();
    timerInterval = setInterval(function printTime(){
        elapsedTime = Date.now() - startTime;
        document.getElementById("stopwatch").innerHTML = timeToString(elapsedTime);
    }, 10)
}

function pause (){
    clearInterval(timerInterval);
}


function timeToString(time) {
  let diffInHrs = time / 3600000;
  let hh = Math.floor(diffInHrs);

  let diffInMin = (diffInHrs - hh) * 60;
  let mm = Math.floor(diffInMin);

  let diffInSec = (diffInMin - mm) * 60;
  let ss = Math.floor(diffInSec);

  let diffInMs = (diffInSec - ss) * 100;
  let ms = Math.floor(diffInMs);

  let formattedMM = mm.toString().padStart(2, "0");
  let formattedSS = ss.toString().padStart(2, "0");
  let formattedMS = ms.toString().padStart(2, "0");

  return `${formattedMM}:${formattedSS}:${formattedMS}`;
}
