class Spot 
{
  float x, y, radius, speed;

  Spot() 
  {
    x = 50;
    y = 50;
    radius = 30;
    speed = 10;
  }
  Spot(float x, float y, float _r) 
  {
    this.x = x;
    this.y = y;
    this.radius = _r;
    speed = 10;
  }

  void display()
  {
    ellipse(x, y, radius, radius);
  }
  
  void move()
  {
    this.x += speed * 0.98;
    this.y += speed * 1.2;
  }
  
  void speed(float new_speed)
  {
    this.speed = new_speed;
  }
}
