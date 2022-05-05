 //globals
 
 //setup
 void setup()
 {
   surface.setResizable(true);
   size(500,500);
   background(255);
 }
 
 //draw
 void draw()
 {
//reset stroke and fill
   noStroke();
   fill(255);
   rect(0,0,500,500);
  
//outer circle
   ellipseMode(RADIUS);
   stroke(0);
   strokeWeight(1);
   fill(255);
   
   ellipse(250,250,216,216);
   
//sun lines
   strokeWeight(5.5);
   line(250,216,250,198);
   line(218,208,229,224);
   line(200,268,218,261);
   line(250,302,250,285);
   strokeWeight(1);
   line(235,208,238,218);
   line(210,229,220,234);
   line(204,251,215,251);
   line(214,278,222,272);
   line(231,291,236,281);
   
//center circle
   ellipseMode(CENTER);
   stroke(0);
   
   fill(#F6FF00);
   strokeWeight(5.5);
   ellipse(250,250,64,64);
   fill(0);
   strokeWeight(1);
   ellipse(250,250,40,40);
   
   fill(#FBFF90);
   ellipse(250,250,21,21);
   fill(0);
   ellipse(253,250,14.5,18);
   
   
//outer symbols
   ellipseMode(CENTER);
   stroke(0);
   fill(255);

   
   strokeWeight(5);
   ellipse(250,35,50,50);
   strokeWeight(0.5);
   ellipse(250,34,36,36);
   ellipse(250,34,30,30);
   line(240,45,261,24);
   line(251,35,261,45);
   strokeWeight(2);
   ellipse(211,35,24,24);
   ellipse(289,35,24,24);
   ellipse(211,35,23,4);
   ellipse(211,35,4,23);
   ellipse(289,35,23,4);
   ellipse(289,35,4,23);
   
   
   strokeWeight(5);
   ellipse(46,185,50,50);
   strokeWeight(0.5);
   ellipse(46,185,36,36);
   ellipse(46,185,30,30);
   line(35,195,56,173);
   line(46,184,56,194);
   strokeWeight(2);
   ellipse(33,223,24,24);
   ellipse(56,146,24,24);
   ellipse(33,223,23,4);
   ellipse(33,223,4,23);
   ellipse(56,146,23,4);
   ellipse(56,146,4,23);
   
   
   strokeWeight(5);
   ellipse(457,184,50,50);
   strokeWeight(0.5);
   ellipse(457,184,36,36);
   ellipse(457,184,30,30);
   line(466,173,446,195);
   line(456,184,467,194);
   strokeWeight(2);
   ellipse(443,145,24,24);
   ellipse(469,223,24,24);
   ellipse(443,145,23,4);
   ellipse(443,145,4,23);
   ellipse(469,223,23,4);
   ellipse(469,223,4,23);
   
   
   strokeWeight(5);
   ellipse(124,425,50,50);
   strokeWeight(0.5);
   ellipse(124,425,36,36);
   ellipse(124,425,30,30);
   line(134,414,114,434);
   line(124,424,134,434);
   strokeWeight(2);
   ellipse(157,449,24,24);
   ellipse(91,401,24,24);
   ellipse(157,449,23,4);
   ellipse(157,449,4,23);
   ellipse(91,401,23,4);
   ellipse(91,401,4,23);
   
   
   strokeWeight(5);
   ellipse(378,425,50,50);
   strokeWeight(0.5);
   ellipse(378,425,36,36);
   ellipse(378,425,30,30);
   line(388,414,367,434);
   line(388,434,377,424);
   strokeWeight(2);
   ellipse(412,401,24,24);
   ellipse(344,449,24,24);
   ellipse(412,401,23,4);
   ellipse(412,401,4,23);
   ellipse(344,449,23,4);
   ellipse(344,449,4,23);
   
   
// inner lines and circles
   ellipseMode(CENTER);
   
   stroke(0);
   fill(255);
   strokeWeight(2);
   line(237,78,161,311);
   fill(#FFF25D);
   ellipse(236,77,30,30);
   ellipse(161,311,30,30);
   fill(200,0,0);
   triangle(236,63,248,84,225,84);
   triangle(161,298,173,317,150,317);
   
   stroke(0);
   fill(255);
   strokeWeight(2);
   line(82,211,281,354);
   fill(0);
   ellipse(80,211,30,30);
   ellipse(281,354,30,30);
   fill(200,0,0);
   ellipse(80,211,14,26);
   ellipse(281,354,14,26);
   
   stroke(0);
   fill(255);
   strokeWeight(2);
   line(414,184,165,184);
   fill(#FFF25D);
   ellipse(414,183,30,30);
   ellipse(165,184,30,30);
   fill(200,0,0);
   triangle(165,170,177,190,153,190);
   triangle(402,190,427,190,414,170);
   fill(#29BDFF);
   ellipse(165,184,15,10);
   ellipse(415,184,15,10);
   
   stroke(0);
   fill(255);
   strokeWeight(2);
   line(161,399,360,253);
   fill(#29BDFF);
   ellipse(159,400,30,30);
   ellipse(359,253,30,30);
   strokeWeight(1);
   fill(0);
   ellipse(159,400,15,15);
   ellipse(359,253,15,15);
   fill(200,0,0);
   ellipse(159,400,4,7);
   ellipse(359,253,4,7);
   
   stroke(0);
   fill(255);
   strokeWeight(2);
   line(288,147,364,383);
   fill(0);
   ellipse(363,384,30,30);
   ellipse(287,147,30,30);
   fill(#29BDFF);
   quad(349,384,363,371,376,384,363,397);
   quad(274,147,287,135,299,147,287,160);
   
   
   noFill();
   
   
//reset stroke and fill
   noStroke();
   noFill();
 }
