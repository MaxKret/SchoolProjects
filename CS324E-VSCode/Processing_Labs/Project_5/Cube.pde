class Cube{
  int t, startY, currentY, endY;
  float angle = 0;
  int x = width/2;
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
    fill(255);
    body = createShape(BOX, t, t, t);
  }
  
  void drawPyramid(){
    if(currentY >= endY){
      pushMatrix();
      translate(x, currentY, 0);
      rotateX(PI/2);
      rotateZ(angle);
      shape(body);
      popMatrix();
      
      angle -=0.55;
      currentY -= 1;
    } else{
      pushMatrix();
      translate(x, endY, 0);
      rotateX(PI/2);
      rotateZ(0.4);
      shape(body);
      popMatrix();
      
      angle = 0;
      
    }
  }
}
