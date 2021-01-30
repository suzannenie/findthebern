'use strict';

var socket = io();

socket.on('connect', function() {
    console.log("connected")
    socket.emit('my event', {data: 'I\'m connected!'});
});