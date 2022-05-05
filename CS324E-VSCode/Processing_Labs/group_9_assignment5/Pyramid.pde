class Pyramid
{
  int t, startY, currentY, endY;
  float angle = 0;
  int x = width/2;
  boolean is_finished = false;
  PShape py;
  
  //default constructor
  Pyramid(){}
  
  //constructor
  Pyramid(int t, int startY, int endY){
    this.t = t;
    this.currentY = startY;
    this.startY = startY;
    this.endY = endY;
    
    stroke(255);
    
    py = createShape();
    py.beginShape(TRIANGLES);
    
    py.fill(164,57,45);
    py.vertex(-t,-t,-t);
    py.vertex(t,-t,-t);
    py.vertex(0,0,t);
    
    py.vertex(t,-t,-t);
    py.vertex(t,t,-t);
    py.vertex(0,0,t);
    
    py.vertex(t,t,-t);
    py.vertex(-t,t,-t);
    py.vertex(0,0,t);
    
    py.vertex(-t,t,-t);
    py.vertex(-t,-t,-t);
    py.vertex(0,0,t);
  
    py.endShape();
  }
  
  void drawPyramid(){
    float f = frameCount;
    if(f%500 == 0)
    {
      reset();
    }
    if(currentY <= endY){
      pushMatrix();
      translate(x, currentY, -100);
      rotateX(PI/2);
      rotateZ(angle);
      shape(py);
      popMatrix();
      
      angle+=0.05;
      currentY += 1;
    } else{
      pushMatrix();
      translate(x, endY, -100);
      rotateX(PI/2);
      shape(py);
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
