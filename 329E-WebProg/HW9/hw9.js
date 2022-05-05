// AJAX
$(function () {
   changeImg();
   do_wait();
});

var timerid;
var playing = true;
var idx = 0;
var top_img = "img1";
var curr_cap = "";
var img_src = new Array("img1", "img2", "img3", "img4", "img5", "img6",
   "img7", "img8", "img9", "img10", "img11");

var img_cap = new Array("Ajanta Ellora", "Hawa Mahal", "Mysore Palace",
   "Taj Mahal", "Agra Fort", "Akshardham Temple",
   "Gateway of India", "Mehrangarh Fort", "Qutub Minar",
   "Sun Temple", "Victoria Memorial Hall");

var playing = true;

function do_wait() {
   timerId = setInterval(() => {
      if (playing == false) { clearInterval(timerId); console.log('timer stopped'); }
      else { changeImg(); }
   }, 3000);
}


function play() { if (!playing) { playing = true; console.log("playing set true"); do_wait(); } }
function pause() { playing = false; console.log("playing set false"); clearInterval(timerId); console.log('pause stopped'); }

function changeImg() {
   var new_img = get_img();
   styleTop = document.getElementById(top_img).style;
   styleNew = document.getElementById(new_img).style;

   cap = document.getElementById("caption");
   cap.textContent = curr_cap;

   styleTop.zIndex = "0";
   styleNew.zIndex = "10";
   top_img = new_img;
}

function get_img() {
   curr_cap = img_cap[idx];
   curr_img = img_src[idx];
   idx += 1;
   console.log("showing #" + idx);
   if (idx == 11) {
      idx = 0;
   }
   return curr_img;
}