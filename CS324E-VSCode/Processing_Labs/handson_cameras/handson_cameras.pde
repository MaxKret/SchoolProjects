float eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ;
boolean center_mode = false;

void setup()
{
  size(800, 500, P3D);
  centerCamera();
  center_mode = false;

}

void mousePressed()
{
  centerCamera();
}

void keyPressed()
{
  
  if (key == CODED)
  {
    
    if(center_mode)
    {
      //centered
      if (keyCode == UP)
      {
        // camera up
        setCamera(eyeX, eyeY-50, eyeZ, centerX, centerY, centerZ, upX, upY, upZ);
      }
      else if (keyCode == DOWN)
      {
        // camera down
        setCamera(eyeX, eyeY+50, eyeZ, centerX, centerY, centerZ, upX, upY, upZ);
      }
      else if (keyCode == RIGHT)
      {
        // camera right
        setCamera(eyeX+50, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ);
      }
      else if (keyCode == LEFT)
      {
        // camera left
        setCamera(eyeX-50, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ);
      }
      else if (keyCode == SHIFT)
      {
        // camera left
        setCamera(eyeX, eyeY, eyeZ-50, centerX, centerY, centerZ, upX, upY, upZ);
      }
      else if (keyCode == CONTROL)
      {
        // camera left
        setCamera(eyeX, eyeY, eyeZ+50, centerX, centerY, centerZ, upX, upY, upZ);
      }
    }
    else
    {
      //non-centered
      if (keyCode == UP)
      {
        // camera up
        setCamera(eyeX, eyeY-50, eyeZ, centerX, centerY-50, centerZ, upX, upY, upZ);
      }
      else if (keyCode == DOWN)
      {
        // camera down
        setCamera(eyeX, eyeY+50, eyeZ, centerX, centerY+50, centerZ, upX, upY, upZ);
      }
      else if (keyCode == RIGHT)
      {
        // camera right
        setCamera(eyeX+50, eyeY, eyeZ, centerX+50, centerY, centerZ, upX, upY, upZ);
      }
      else if (keyCode == LEFT)
      {
        // camera left
        setCamera(eyeX-50, eyeY, eyeZ, centerX-50, centerY, centerZ, upX, upY, upZ);
      }
      else if (keyCode == SHIFT)
      {
        // camera left
        setCamera(eyeX, eyeY, eyeZ-50, centerX, centerY, centerZ-50, upX, upY, upZ);
      }
      else if (keyCode == CONTROL)
      {
        // camera left
        setCamera(eyeX, eyeY, eyeZ+50, centerX, centerY, centerZ+50, upX, upY, upZ);
      }
    }
    
  }
  
  else //key NOT Coded
  {
    if(key == 'c' || key == 'C')
    {
      if(center_mode == true)
      {
        center_mode = false;
      }
      
      else//center_mode == false;
      {
        center_mode = true;
      }
    }
  }
}

void setCamera()
{
  camera(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ);
}

void setCamera(float ix, float iy, float iz, float cx, float cy, float cz, float ux, float uy, float uz)
{
  eyeX = ix;
  eyeY = iy;
  eyeZ = iz;
  centerX = cx;
  centerY = cy;
  centerZ = cz;
  upX = ux;
  upY = uy;
  upZ = uz;
  camera(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ);
}

void centerCamera()
{
  setCamera(width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/2.0, 0, 0, 1, 0);
}


void drawGraph()
{
  line(0, 0, 0, 100, 0, 0);
  text("+X", 100, 0, 0);
  line(0, 0, 0, 0, 100, 0);
  text("+Y", 0, 100, 0);
  line(0, 0, 0, 0, 0, -100);
  text("-Z", 0, 0, -100);
}
void displayText()
{
  text("Click to Reset; C for centered mode: ",0,10,0);
  text("arrow keys for +/-X and +/-Y, shift/ctrl for -Z/+Z respectively",0,30,0);
  if(center_mode == true)
  {
    fill(0,255,0);
    text("ON",210,10,0);
  }
  else//center_mode == false;
  {
    fill(255,0,0);
    text("OFF",210,10,0);
  }
}
void draw()
{
  background(204);
  lights();
  beginCamera();
  setCamera();
  displayText();
  endCamera();

  pushMatrix();
  translate(250, 250, 0);
  stroke(0);
  fill(0);
  drawGraph();
  stroke(0, 255, 0, 127);
  fill(0, 255, 100);
  sphere(50);
  popMatrix();
  
  pushMatrix();
  translate(400, 250, -50);
  stroke(0);
  fill(0);
  drawGraph();
  stroke(255, 0, 0, 127);
  fill(255, 100, 0);
  box(50);
  popMatrix();
  
  pushMatrix();
  translate(400, 212, -50);
  stroke(0);
  fill(0);
  drawGraph();
  stroke(0, 0, 255, 127);
  fill(0, 100, 255);
  box(25);
  popMatrix();
  
  pushMatrix();
  translate(500, 250, 100);
  stroke(0);
  fill(0);
  drawGraph();
  stroke(255, 0, 0, 127);
  fill(255, 0, 0);
  box(75);
  popMatrix();
  
}
