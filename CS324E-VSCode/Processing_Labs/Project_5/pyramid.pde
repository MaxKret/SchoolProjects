class pyramid{
  int t, startY, currentY, endY;
  float angle = 0;
  int x = width/2;
  PShape py;
  
  //default constructor
  pyramid(){}
  
  //constructor
  pyramid(int t, int startY, int endY){
    this.t = t;
    this.currentY = startY;
    this.startY = startY;
    this.endY = endY;
    
    stroke(255);
    
    py = createShape();
    py.beginShape(TRIANGLES);
    
    py.fill(255);
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
    if(currentY <= endY){
      pushMatrix();
      translate(x, currentY, 0);
      rotateX(PI/2);
      rotateZ(angle);
      shape(py);
      popMatrix();
      
      angle+=0.05;
      currentY += 1;
    } else{
      pushMatrix();
      translate(x, endY, 0);
      rotateX(PI/2);
      rotateZ(0.4);
      shape(py);
      popMatrix();
      
      angle = 0;
      
    }
  }
}
