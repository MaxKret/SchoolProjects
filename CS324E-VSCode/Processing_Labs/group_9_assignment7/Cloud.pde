class Cloud{
  PShape cloud;
  int startX;
  int startY;
  int currentX;
  int currentY;
  float descentSpeed;
  
  Cloud(int startX, int startY, float descentSpeed){
    this.startX = startX;
    this.startY = startY;
    this.currentX = startX;
    this.currentY = startY;
    this.descentSpeed = descentSpeed;  
  }
  
  void descend(){
    if (this.currentY < 750){
      this.currentY += descentSpeed;
    } else{
      this.currentY = startY;
      this.currentX = int(random(540))-20;
    }
  }
  
  void display(){
    
    //create cloud
    fill(255);
    cloud = createShape(PShape.PATH);
    cloud.beginShape();
    cloud.vertex(currentX,currentY);
    cloud.vertex(currentX,currentY+20);
    cloud.vertex(currentX+80,currentY+20);
    cloud.vertex(currentX+80,currentY-10);
    cloud.vertex(currentX+40,currentY-10);
    cloud.vertex(currentX+40,currentY);
    cloud.vertex(currentX,currentY);
    cloud.endShape();
    shape(cloud);
  }
}
