Resources x = new Resources();
PImage img;
void setup(){
  size(500,500);
  img = loadImage("resource.png");
}

void draw(){
  background(255);
  x.displayAll();
  
  // test code
  //x.drainAllHealth(0,0);
  //Resource z = x.getNearest(0,0);
  //if (z != null){
  //  print("The closest resource to (0,0) is", z.xLoc, z.yLoc, "\n");
  //}
}

void mousePressed(){
  Resource temp = new Resource(mouseX,mouseY,img);
  x.addResource(temp);
}
