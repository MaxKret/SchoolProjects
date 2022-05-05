class TwoSpots extends Spot
{
  float offset;
  
  TwoSpots(float x, float y, float radius, float speed, float xDir, float yDir, float offset)
  {
    super(x,y,radius,speed,xDir,yDir);
    this.offset = offset;
  }
  
  void display()
  {
    super.display(x - offset, y);
    super.display(x + offset, y);
  }
  
}
