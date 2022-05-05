//globals
//  camera
float eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ;
boolean center_mode = false;
//  scene / pos
color ground_color = color(#70391F);
float center_pos_x, center_pos_y, center_pos_z;

// class objects
Window window;
Door door;
Pyramid py;
Cube cb;

void setup() 
{
  size(800, 500, P3D);
  centerCamera();
  center_mode = false;
  
  ground_color = color(#70391F);
  center_pos_x = width/2;
  center_pos_y = 374; //height*.75-1
  center_pos_z = 0;
  
  //                  /Xo,Yo,Zo,DEGo Xf,Yf,Zf, DEGf
  window = new Window(310,250,80, 0, 330,250,0, 720);
  door = new Door(370,270,80, -90, 370,270,0, 0);
  //             size,  Yo,   Yf
  py = new Pyramid(110, -300, 100);
  //              r,  Yo,  Yf
  cb = new Cube(200, 600, 301);
}
void draw() 
{
  background(204);
  lights();
  drawGraph(width,height);
  setCamera();
  displayText();
  
  // GROUND / FLOOR
  fill(0);
  stroke(0);
  pushMatrix();
  translate(center_pos_x, center_pos_y+1, center_pos_z);//translate to center of box
  fill(ground_color);
  box(width,10,height);
  popMatrix();
  
  /*if(py.is_finished)
  {
    delay(1000);
  }*/
  
  // OBJECTS
  door.display(); //<>//
  window.display();
  py.drawPyramid();
  cb.drawPyramid();

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
void drawGraph(float x, float y)
{
  line(0, 0, 0, x, 0, 0);
  text("+X", x, 0, 0);
  line(0, 0, 0, 0, y, 0);
  text("+Y", 0, y, 0);
  line(0, 0, 0, 0, 0, -500);
  text("-Z", 0, 0, -500);
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
