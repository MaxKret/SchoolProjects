float wwidth, wheight,x_init, y_init, z_init,angle_init;
float x_curr,y_curr,z_curr,angle_curr;
float x_final,y_final,z_final,angle_final;
float f,i;
PShape rec;

void setup()
{
  size(800,500,P3D);
  
  x_init = 280;
  y_init = 250;
  z_init = 1;
  angle_init = 1;
  
  x_curr = x_init;
  y_curr = y_init;
  z_curr = z_init;
  angle_curr = angle_init;
  
  x_final = 280;
  y_final = 250;
  z_final = 50;
  angle_final = 90;
  
  rec = createShape(RECT, 0,0,20,30);
}

void draw()
{
  background(204);
  lights(); //<>//
  
  println(frameCount);
  
  if(frameCount < 20)
  {
    f = frameCount;
    i = f/20;
    x_curr = lerp(x_init,x_final,i);
    y_curr = lerp(y_init,y_final,i);
    z_curr = lerp(z_init,z_final,i);
    angle_curr = lerp(angle_init,angle_final,i);
  }
  
  pushMatrix();
  translate(x_curr,y_curr,z_curr);
  rotateZ(radians(angle_curr));
  shape(rec, 0, 0);
  popMatrix();
}
