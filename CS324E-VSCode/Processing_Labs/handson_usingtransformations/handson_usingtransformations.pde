void setup()
{
  size(500,500);
  background(200);
}

void draw()
{
  fill(255);
  rect(0,0,50,40);
  
  pushMatrix(); // translate to middle of screen(red)
  fill(255,0,0);
  translate(250,250);
  rect(0,0,50,40);
  popMatrix();
  
  pushMatrix(); // scale->translate (orange)
  fill(255,100,0);
  scale(1.3);
  translate(100,0);
  rect(0,0,50,40);
  popMatrix();
  
  pushMatrix(); // scale->rotate->translate (green)
  fill(0,255,0);
  scale(1.9);
  rotate(radians(30));
  translate(70,80);
  rect(0,0,50,40);
  popMatrix();
  
  pushMatrix(); // scale->translate->rotate (blue)
  fill(0,0,255);
  scale(0.5);
  translate(400,400);
  rotate(-0.5);
  rect(0,0,50,40);
  popMatrix();
  
  fill(255,0,255);
  rect(0,0,20,60);
  pushMatrix(); // additional object (purple)
  scale(1.6);
  translate(250,250);
  rotate(radians(90));
  rect(0,0,20,60);
  popMatrix();
}
