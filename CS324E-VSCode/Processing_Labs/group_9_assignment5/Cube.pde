class Cube{
  int t, startY, currentY, endY;
  float angle = 0;
  int x = width/2;
  boolean is_finished;
  PShape body;
  
  //default constructor
  Cube(){}
  
  //constructor
  Cube(int t, int startY, int endY){
    this.t = t;
    this.currentY = startY;
    this.startY = startY;
    this.endY = endY;
    
    stroke(255);
    fill(226,195,73);
    body = createShape(BOX, t, t, t);
  }
  
  void drawPyramid()
  {
    float f = frameCount;
    if(f%500 == 0)
    {
      reset();
    }
    if(currentY >= endY){
      pushMatrix();
      translate(x, currentY, -100);
      rotateX(PI/2);
      rotateZ(angle);
      shape(body);
      popMatrix();
      
      angle -=0.55;
      currentY -= 1;
    } else{
      pushMatrix();
      translate(x, endY, -100);
      rotateX(PI/2);
      shape(body);
      popMatrix();
      is_finished = true;
      
    }
  }
  
  void reset()
  {
    currentY = startY;
    angle = 0;
    is_finished = false;
  }
}
