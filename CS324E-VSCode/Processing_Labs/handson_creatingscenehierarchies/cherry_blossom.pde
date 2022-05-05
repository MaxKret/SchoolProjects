class cherry_blossom{
  //establish values
  float startX, startY, currentX, currentY, angle = 0, startAngle;
  PShape blossom;
  
  //default constructor
  cherry_blossom(){}
  
  //constructor
  cherry_blossom(float startX, float startY, float startAngle){
    this.startX = startX;
    this.startY = startY;
    this.currentY = startY;
    this.currentX = startX;
    this.startAngle = startAngle;
    this.angle = startAngle;
    
    fill(228,146,231);
    //create blossom shape
    blossom = createShape();
    blossom.beginShape();
    blossom.vertex(currentX,currentY); 
    blossom.vertex(currentX-5,currentY+10); 
    blossom.vertex(currentX+3,currentY+20); 
    blossom.vertex(currentX+10,currentY+25); 
    blossom.vertex(currentX+15,currentY+26); 
    blossom.vertex(currentX+12,currentY+10); 
    blossom.vertex(currentX,currentY); 
    blossom.endShape();
  }
  
  void fall(float rotationRate, float xRate, float yRate){
    
    //fill(228,146,231);
    pushMatrix();
    translate(currentX, currentY);
  
    pushMatrix();
    scale(0.8);
    translate(150, 0);
    rotate(angle);
    shape(blossom);
    popMatrix();
    popMatrix();
    angle += rotationRate;
    currentX += xRate;
    currentY += yRate;
    
    //to reset blossom
    if (currentY >= 640 || currentX >= 1060){
      currentX = startX;
      currentY = startY;
      angle = startAngle;
    }
  }
}
