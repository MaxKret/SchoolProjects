ColoredSpot csp1;
ColoredSpot csp2;
TwoSpots tsp1;
TwoSpots tsp2;

void setup() {
  size(300, 300);
  //noLoop();
  color c1 = color(255,0,0);
  csp1 = new ColoredSpot(20,20,20,20,1,1,c1);
  color c2 = color(0,255,0);
  csp2 = new ColoredSpot(40,20,20,20,1,1,c2);
  
  tsp1 = new TwoSpots(80,100,20,20,0,1,15);
  tsp2 = new TwoSpots(220,200,20,20,0,-1,15);
}

void draw() 
{
  csp1.display();
  csp2.display();
  tsp1.display();
  tsp2.display();
  
  tsp1.move();
  tsp2.move();
  
}
