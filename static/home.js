'use strict';

var slideIndex = 0;
let x = document.getElementsByClassName("slides");
carousel();

function carousel() {
  var i;
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > x.length) {slideIndex = 1}
  console.log("slideindex", slideIndex)
  x[slideIndex-1].style.display = "";
  setTimeout(carousel, 2000); // Change image every 2 seconds
}