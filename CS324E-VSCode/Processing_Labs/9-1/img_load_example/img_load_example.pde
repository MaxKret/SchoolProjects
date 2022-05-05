PImage img1;
PImage img2;
PImage img3;
PImage img4;
String path = "C:\\Users\\Crackhead\\Desktop\\College Stuff\\CS324E\\Processing_Labs\\";

void setup()
{
  background(255);
  surface.setResizable(true);
  img1 = loadImage(path+"test.jpg");
  img2 = loadImage(path+"test.jpg");
  img3 = loadImage(path+"test.jpg");
  img4 = loadImage(path+"test.jpg");
  surface.setSize((img1.width)*4, (img1.height)*4);
  
}

void draw()
{
  noStroke();
  noFill();
  
  tint(#FF5053,150);
  image(img1, 0, 0);
  frame(0,0,259,194);
  
  tint(#00FF63,150);
  image(img2, 261, 0);
  frame(261,0,259,194);
  
  tint(#00ECFF,150);
  image(img3, 0, 196);
  frame(0,196,259,194);
  
  tint(#F6FF00,150);
  image(img4, 261, 196);
  frame(261,196,259,194);
  
  noStroke();
  noFill();
}

void frame(int x, int y, int w, int l)
{
  stroke(0);
  strokeWeight(1.5);
  fill(0,0,0,0);
  rect(x,y,w,l);
  noStroke();
  noFill();
}
