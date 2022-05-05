class ColoredSpot extends Spot
{
  color c;
  
  ColoredSpot(){}
  
  ColoredSpot(float x, float y, float radius, float speed, float xDir, float yDir, color c)
  {
    super(x,y,radius,speed,xDir,yDir);
    this.c = c;
  }
  
  void display()
  {
    fill(c);
    super.display();
    fill(255);
  }
  
}
