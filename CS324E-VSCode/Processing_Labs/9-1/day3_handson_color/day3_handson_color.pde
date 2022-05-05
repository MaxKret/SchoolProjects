PImage img1;
PImage img2;
PImage img3;
PImage img4;
String path = "C:\\Users\\Crackhead\\Desktop\\College Stuff\\CS324E\\Processing_Labs\\";

color R = #FF5053;
color Oy = #F6FF00;
color G = #00FF63;
color B = #00ECFF;
color[] ROyGB ={R, Oy, G, B};

void setup()
{
  background(255);
  surface.setResizable(true);
  img1 = loadImage(path+"test.jpg");
  img2 = loadImage(path+"test.jpg");
  img3 = loadImage(path+"test.jpg");
  img4 = loadImage(path+"test.jpg");
  surface.setSize(img1.width, img1.height);
}

void draw()
{
  noStroke();
  noFill();
  
  popArt();
  colorfulShapes();
  
  noStroke();
  noFill();
}


void popArt()
{
  noStroke();
  noFill();
  
  tint(ROyGB[0],150);
  image(img1, 0, 0);
  frame(0,0,698,698);
  
  tint(ROyGB[2],150);
  image(img2, 700, 0);
  frame(700,0,698,698);
  
  tint(ROyGB[3],150);
  image(img3, 0, 700);
  frame(0,700,698,698);
  
  tint(ROyGB[1],150);
  image(img4, 700, 700);
  frame(700,700,698,698);
  
  noStroke();
  noFill();
}

void colorfulShapes()
{
  noStroke();
  noFill();
  
  fill(0);
  stroke(0);
  strokeWeight(4);
  rectMode(CORNERS);
  ellipseMode(CORNERS);
  
  fill(ROyGB[2]);
  stroke(ROyGB[1]);
  rect(696,696,549,549);
  fill(ROyGB[3]);
  blendMode(REPLACE);
  ellipse(696,696,549,549);
  blendMode(BLEND);
  
  fill(ROyGB[0]);
  stroke(ROyGB[3]);
  rect(700,700,847,549);
  blendMode(REPLACE);
  ellipse(700,700,847,549);
  blendMode(BLEND);
  
  fill(ROyGB[1]);
  stroke(ROyGB[2]);
  rect(696,696,549,847);
  blendMode(REPLACE);
  ellipse(696,696,549,847);
  blendMode(BLEND);
  
  fill(ROyGB[3]);
  stroke(ROyGB[0]);
  rect(700,700,847,847);
  blendMode(REPLACE);
  ellipse(700,700,847,847);
  blendMode(BLEND);
  
  noStroke();
  noFill();
  strokeWeight(1);
  rectMode(CORNER);
  ellipseMode(CENTER);
}

void frame(int x, int y, int w, int l)
{
  noStroke();
  noFill();
  stroke(0);
  strokeWeight(1.5);
  fill(0,0,0,0);
  rect(x,y,w,l);
  noStroke();
  noFill();
  strokeWeight(1);
}
