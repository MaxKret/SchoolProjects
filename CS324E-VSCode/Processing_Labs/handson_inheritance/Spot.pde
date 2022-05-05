class Spot 
{
  float x, y, radius, speed;
  float xDir, yDir;

  Spot() {}
  
  Spot(float x, float y, float radius, float speed) 
  {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.speed = speed;
    this.xDir = 1;
    this.yDir = 1;
  }
  
  Spot(float x, float y, float radius, float speed, float xDir, float yDir) 
  {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.speed = speed;
    this.xDir = xDir;
    this.yDir = yDir;
  }

  void display()
  {
    ellipse(x, y, radius, radius);
  }
  
  void display(float x, float y)
  {
    ellipse(x, y, radius, radius);
  }
  
  void move()
  {
    this.x += speed * xDir;
    this.y += speed * yDir;
    constrain(x, 0, 300);
    constrain(y, 0, 300);
  }
  
  void speed(float new_speed)
  {
    this.speed = new_speed;
  }
}
