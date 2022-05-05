// AJAX
$(function () {
	changeImg()
})

var top_img = "img1";
var curr_cap = "Galaxy Cluster"
var img_src = new Array ("img1", "img2", "img3", "img4", "img5", "img6");
var img_cap = new Array ("Galaxy Cluster", "M 104", "NGC 1300", "Interacting Galaxies", "M 51", "NGC 6217")

function get_img () {
   var rnd_idx = Math.trunc (Math.random() * img_src.length);
   curr_cap = img_cap[rnd_idx];
   return img_src[rnd_idx];
}

function changeImg() {
   var new_img = get_img();
   styleTop = document.getElementById(top_img).style;
   styleNew = document.getElementById(new_img).style;

   cap = document.getElementById("caption")
   cap.textContent = curr_cap;

   styleTop.zIndex = "0";
   styleNew.zIndex = "10";
   top_img = new_img;
}
