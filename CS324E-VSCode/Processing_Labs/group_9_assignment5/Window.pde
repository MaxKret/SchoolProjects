class Window
{
  float wwidth, wheight,x_init, y_init, z_init,angle_init;
  float x_curr,y_curr,z_curr,angle_curr;
  float x_final,y_final,z_final,angle_final;
  float f,step,step_size;
  boolean is_finished;
  PShape window = createShape(GROUP);
  
  
  Window(float _x_init, float _y_init, float _z_init, float _angle_init,
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
    
    wwidth = 45;
    wheight = 50;
    
    step_size = 500;
    
    fill(161,0,0);
    
    PShape vertical_border = createShape(BOX, 5, wheight-5, 2);
    PShape horizontal_border = createShape(BOX, wwidth-5, 5, 2);
    
    pushMatrix();
    PShape left_border = createShape(BOX, 5, wheight+5, 2);
    left_border.translate(-wwidth/2, 0, 0);
    popMatrix();
    
    pushMatrix();
    PShape right_border = createShape(BOX, 5, wheight+5, 2);
    right_border.translate(wwidth/2, 0, 0);
    popMatrix();
    
    pushMatrix();
    PShape top_border = createShape(BOX, wwidth+5, 5, 2);
    top_border.translate(0, -wheight/2, 0);
    popMatrix();
    
    pushMatrix();
    PShape bottom_border = createShape(BOX, wwidth+5, 5, 2);
    bottom_border.translate(0, wheight/2, 0);
    popMatrix();
    
    window.addChild(vertical_border);
    window.addChild(horizontal_border);
    window.addChild(left_border);
    window.addChild(right_border);
    window.addChild(top_border);
    window.addChild(bottom_border);
     
  }
  
  void move()
  {
    if((frameCount%step_size) < step_size)
    {
      f = (frameCount%step_size); //<>//
      step = f/step_size;
      x_curr = lerp(x_init,x_final,step); //<>//
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
    pushMatrix(); //<>//
    translate(x_curr,y_curr,z_curr);
    rotateZ(radians(angle_curr));
    shape(window, 0, 0);
    popMatrix();
    
  }
}
