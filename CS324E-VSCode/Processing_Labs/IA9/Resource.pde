class Resource{
  PImage img;
  int xLoc;
  int yLoc;
  int health = 500;
  
  Resource(int x, int y, PImage img){
    this.xLoc = x;
    this.yLoc = y;
    this.img = img;
  }
  
  boolean drainHealth(float x,float y){
    if((xLoc-16<x) && (x<xLoc+16) && (yLoc-16<y) && (y<yLoc+16)){
      health -= 1;
      return true;
    }
    return false;
  }
  
  void display(){
    tint(255,(255*health/500));
    //have minus 16 to get center of image where clicked
    image(img,xLoc-16,yLoc-16);
  }
  

  
  
}
