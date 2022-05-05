void setup()
{
  size(200, 200);
  background(255);
}

void draw()
{
  // set default
  stroke(0);
  fill(255);
  rectMode(CORNER);
  ellipseMode(CENTER);
  
  // draw order
  stroke(0);
  fill(200);
  rect(10, 5, 30, 20);
  fill(100);
  rect(0, 0, 30, 20);
  noFill();
  
  // fill and stroke
  fill(255);
  rect(75,75,50,55);
  fill(100);
  rect(75,130,50,55);
  noFill();
  ellipse(100,100,20,25);
  fill(200);
  ellipse(100,150,20,25);
  fill(150);
  triangle(100,110,110,125,90,125);
  triangle(100,165,110,180,90,180);
  stroke(#FF0004);
  quad(20,100,40,150,60,150,40,100);
  stroke(0);
  quad(180,100,160,150,140,150,160,100);
  arc(25,175,50,50,3.14,6.28);
  fill(0);
  arc(175,175,50,50,3.14,6.28);
  noStroke();
  fill(200);
  rect(150,20,15,20);
  
  // modes
  stroke(0);
  fill(255);
  
  rectMode(CORNER); //default mode for rects
  rect(100,10,10,10);
  rectMode(CENTER);
  rect(100,10,10,10);
  
  ellipseMode(CENTER); //default mode for ellipses
  ellipse(100,30,10,15);
  ellipseMode(CORNER);
  ellipse(100,30,10,15);

  // return to default
  stroke(0);
  fill(255);
  rectMode(CORNER);
  ellipseMode(CENTER);
}
