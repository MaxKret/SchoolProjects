void setup() {
  size(200, 200);
  //noLoop();
}
void draw() 
{
  Spot sp = new Spot(0, 0, 15);
  sp.display();
  sp.move();
  sp.display();
  sp.move();
  sp.display();
  sp.move();
  sp.display();
  sp.move();
  sp.display();
  sp.speed(20);
  sp.move();
  sp.display();
  sp.move();
  sp.display();
  sp.display();
  sp.move();
  sp.display();
  sp.move();
  sp.speed(30);
  sp.move();
  sp.display();
  Spot spt = new Spot(200, 200, 15);
  spt.speed(-10);
  spt.display();
  spt.move();
  spt.display();
  spt.move();
  spt.display();
  spt.move();
  spt.display();
  spt.move();
  spt.display();
  spt.speed(-20);
  spt.move();
  spt.display();
  spt.move();
  spt.display();
  spt.display();
  spt.move();
  spt.display();
  spt.move();
  spt.speed(-30);
  spt.move();
  spt.display();
}
