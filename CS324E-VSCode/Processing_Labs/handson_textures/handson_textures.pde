float dr, dg, db;
float pr, pg, pb;
float sr, sg, sb;
float ar, ag, ab;
boolean d_mode,p_mode,s_mode,a_mode = false;
float r,g,b;
PImage tex;

void setup() 
{
  size(800, 500, P3D);
  tex = loadImage("texture.jpg");
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
  background(20);
  displayUserIn();
  
  //textures
  
  pushMatrix();//normal
  translate(width*.5, 10, 0);
  stroke(0);
  fill(255);
  textureMode(NORMAL); 
  textureWrap(CLAMP);
  beginShape();
  texture(tex);
  vertex(0, 0, 0, 0, 0);
  vertex(50, 0, 0, 1, 0);
  vertex(50, 70, 0, 1, 1);
  vertex(0, 70, 0, 0, 1);
  endShape();
  popMatrix();
  
  pushMatrix();//image
  translate(width*.5+60, 10, 0);
  stroke(0);
  fill(255);
  textureMode(IMAGE);
  textureWrap(CLAMP);
  beginShape();
  texture(tex);
  vertex(0, 0, 0, 0, 0); // 50=698; 1 = 698
  vertex(50, 0, 0, 698, 0);
  vertex(50, 70, 0, 698, 977.2); // 70 * (698/50) = 977.2
  vertex(0, 70, 0, 0, 977.2);
  endShape();
  popMatrix();
  
  pushMatrix();//clamp
  translate(width*.5+120, 10, 0);
  stroke(0);
  fill(255);
  textureMode(NORMAL);
  textureWrap(CLAMP);
  beginShape();
  texture(tex);
  vertex(0, 0, 0, 0, 0);
  vertex(50, 0, 0, 1, 0);
  vertex(50, 70, 0, 1, 1.25);
  vertex(0, 70, 0, 0, 1.25);
  endShape();
  popMatrix();
  
  pushMatrix();//repeat
  translate(width*.5+180, 10, 0);
  stroke(0);
  fill(255);
  textureMode(NORMAL);
  textureWrap(REPEAT);
  beginShape();
  texture(tex);
  vertex(0, 0, 0, 0, 0);
  vertex(50, 0, 0, 1, 0);
  vertex(50, 70, 0, 1, 1.25);
  vertex(0, 70, 0, 0, 1.25);
  endShape();
  popMatrix();
  
  //lighting and materials
  
  lightSpecular(0, 255, 0);
  
  directionalLight(dr, dg, db, -1, 1, 0); // top right
  pointLight(pr,pg,pb,width,height,0); // bottom right
  spotLight(sr,sg,sb, 0,height,0, 1,-1,0, radians(30),0.5); // bottom left
  ambientLight(ar,ag,ab,0,0,0); // top left

  /*ambient(r,g,b);
    specular(r, g, b) //color of highlights
    shininess(s) //amount of highlight
    lightSpecular(r, g, b) //specular light color*/

  pushMatrix(); //<>//
  translate(250, 250, 0);
  noStroke();
  fill(255);
  specular(150,255,0);
  ambient(0,10,0);
  shininess(10000);
  sphere(50);
  popMatrix();
  
  pushMatrix();
  translate(400, 250, -50);
  rotateY(radians(30));
  stroke(255, 0, 0, 127);
  specular(255,0,0);
  ambient(0,20,20);
  shininess(1000);
  fill(200,0,0);
  box(50);
  popMatrix();
  
  pushMatrix();
  translate(400, 215, -50);
  rotateY(radians(-30));
  stroke(0, 0, 255, 127);
  fill(0,0,200);
  ambient(0,0,20);
  shininess(100);
  specular(0,255,100);
  box(25);
  popMatrix();
  
  pushMatrix();
  translate(500, 250, 100);
  stroke(255, 0, 0, 127);
  fill(255);
  shininess(10);
  ambient(0,0,50);
  specular(0,0,255);
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
