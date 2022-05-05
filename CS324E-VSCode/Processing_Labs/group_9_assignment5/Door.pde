class Door
{
  float dwidth, dheight, x_init, y_init, z_init,angle_init;
  float x_curr,y_curr,z_curr,angle_curr;
  float x_final,y_final,z_final,angle_final;
  float f,step,step_size;
  boolean is_finished;
  PShape door = createShape(GROUP);
  
  
  Door(float _x_init, float _y_init, float _z_init, float _angle_init,
       float _x_final,float _y_final,float _z_final,float _angle_final)
  {
    x_init = _x_init;
    y_init = _y_init;
    z_init = _z_init;
    angle_init = _angle_init;
    
    x_curr = x_init;
    y_curr = y_init;
    z_curr = z_init;
    angle_curr = angle_init;
    
    x_final = _x_final;
    y_final = _y_final;
    z_final = _z_final;
    angle_final = _angle_final;
    
    dwidth = 60;
    dheight = 100;
    
    step_size = 500;
    
    pushMatrix();
    stroke(0);
    fill(161,130,206);
    PShape doorBox = createShape(BOX, dwidth, dheight, 4);
    doorBox.translate(30,50,0);
    noStroke();
    fill(0);
    PShape handle = createShape(SPHERE, 4);
    handle.translate(dwidth-10, 50, 5);
    popMatrix();
    
    door.addChild(doorBox);
    door.addChild(handle);
     
  }
  
  void move()
  {
    if((frameCount%step_size) < step_size)
    {
      f = (frameCount%step_size);
      step = f/step_size;
      x_curr = lerp(x_init,x_final,step);
      y_curr = lerp(y_init,y_final,step);
      z_curr = lerp(z_init,z_final,step);
    }
  }
  
  void spin()
  {
    if((frameCount%step_size) < step_size)
    {
      f = (frameCount%step_size);
      step = f/step_size;
      angle_curr = lerp(angle_init,angle_final,step);
    }
  }
  
  void display()
  {
    move();
    spin();
    pushMatrix();
    translate(x_curr,y_curr,z_curr);
    rotateY(radians(angle_curr));
    shape(door, 0, 0);
    popMatrix();
  }
}
