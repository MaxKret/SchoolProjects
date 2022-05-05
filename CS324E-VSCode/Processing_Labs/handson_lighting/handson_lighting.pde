float dr, dg, db;
float pr, pg, pb;
float sr, sg, sb;
float ar, ag, ab;
boolean d_mode,p_mode,s_mode,a_mode = false;
float r,g,b;
void setup() 
{
  size(800, 500, P3D);
  d_mode = false;
  p_mode = false;
  s_mode = false;
  a_mode = false;
  r=0;
  g=0;
  b=0;
  ar=255;
  ag=255;
  ab=255;
}
void draw() 
{
  background(0);
  displayUserIn();
  directionalLight(dr, dg, db, -1, 1, 0); // top right
  pointLight(pr,pg,pb,width,height,0); // bottom right
  spotLight(sr,sg,sb, 0,height,0, 1,-1,0, radians(30),0.5); // bottom left
  ambientLight(ar,ag,ab,0,0,0); // top left

  pushMatrix(); //<>//
  translate(250, 250, 0);
  noStroke();
  fill(255);
  sphere(50);
  popMatrix();
  
  pushMatrix();
  translate(400, 250, -50);
  rotateY(radians(30));
  stroke(255, 0, 0, 127);
  fill(255);
  box(50);
  popMatrix();
  
  pushMatrix();
  translate(400, 215, -50);
  rotateY(radians(-30));
  stroke(0, 0, 255, 127);
  fill(255);
  box(25);
  popMatrix();
  
  pushMatrix();
  translate(500, 250, 100);
  stroke(255, 0, 0, 127);
  fill(255);
  box(75);
  popMatrix();
}

void mousePressed()
{
  
  if ((mouseY >= 40 && mouseY <= 80) && (mouseX >= 0 && mouseX <= 255))
  {
    //red
    if(mouseY >= 40 && mouseY <= 50)
    {
      r = mouseX;
    }
    
    //green
    if(mouseY >= 55 && mouseY <= 65)
    {
      g = mouseX;
    }
    
    //blue
    if(mouseY >= 70 && mouseY <= 80)
    {
      b = mouseX;
    }
  }
  
}

void displayUserIn()
{
  text("Use D,P,S,A to select each light",0,10,0);
  text("click on the bars below to change RGB values from 0-255",0,30,0);
  
  fill(255,0,0);
  stroke(255,0,0);
  rect(0,40,255,10);
  text(r,255,50,0);
  
  fill(0,255,0);
  stroke(0,255,0);
  rect(0,55,255,10);
  text(g,255,65,0);
  
  fill(0,0,255);
  stroke(0,0,255);
  rect(0,70,255,10);
  text(b,255,80,0);
  
  fill(255);
  
  if(d_mode == true)
  {
    dr = r;
    dg = g;
    db = b;
    text("A",215,10,0);
    text("S",205,10,0);
    text("P",195,10,0);
    fill(0,255,0);
    text("D",183,10,0);
  }
  if(p_mode == true)
  {
    pr = r;
    pg = g;
    pb = b;
    text("D",183,10,0);
    text("S",205,10,0);
    text("A",215,10,0);
    fill(0,255,0);
    text("P",195,10,0);
  }
  if(s_mode == true)
  {
    sr = r;
    sg = g;
    sb = b;
    text("D",183,10,0);
    text("P",195,10,0);
    text("A",215,10,0);
    fill(0,255,0);
    text("S",205,10,0);
  }
  if(a_mode == true)
  {
    ar = r;
    ag = g;
    ab = b;
    text("D",183,10,0);
    text("P",195,10,0);
    text("S",205,10,0);
    fill(0,255,0);
    text("A",215,10,0);
  }
}

void keyPressed()
{
  
  if (key == CODED)
  {
    
  }
  
  else //key NOT Coded
  {
    if(key == 'd' || key == 'D')
    {
      d_mode = true;
      p_mode = false;
      s_mode = false;
      a_mode = false;
    }
    else if(key == 'p' || key == 'P')
    {
      d_mode = false;
      p_mode = true;
      s_mode = false;
      a_mode = false;
    }
    else if(key == 's' || key == 'S')
    {
      d_mode = false;
      p_mode = false;
      s_mode = true;
      a_mode = false;
    }
    else if(key == 'a' || key == 'A')
    {
      d_mode = false;
      p_mode = false;
      s_mode = false;
      a_mode = true;
    }
  }
}
