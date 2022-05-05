//globals

Particle p1;

float y1,vy1,m1,ry1,ks1;

float m2,ks2;
PVector xy2,v2,r2,f2;


//setup
void setup()
{
  size(900,500);
  ellipseMode(RADIUS);
  
  //p1
  p1 = new Particle(220,height-10,0,0,1,10);
  
  //spring1 - no PVectors  
  m1 = 15.0;
  ks1 = 0.1;
  y1 = 0.0;
  vy1 = 0.0;
  ry1 = 250;
  
  //spring2 - with PVectors
  m2 =15.0;
  ks2 = 0.1;
  xy2 = new PVector(120,0);
  v2 = new PVector();
  r2 = new PVector(150,250);
  f2 = new PVector();
  
}

//draw
void draw()
{
  background(255);
  
  // p3 = single Particle
  p1.display();
  p1.applyForces(0.05,-0.025);
  
  // spring1 - no PVectors
  float f1 = -(ks1 * (y1 - ry1));
  float a1 = f1/m1;
  vy1 = vy1 + a1;
  y1 += vy1;
  rect(10, y1, 100, 20);
  
  
  // spring2 - PVectors
  //float f = -(ks1 * (y1 - ry1));
  f2 = new PVector((xy2.x - r2.x)*ks2*-1, (xy2.y - r2.y)*ks2*-1); //<>//
  PVector a2 = f2.div(m2);
  v2 = v2.add(a2);
  xy2 = xy2.add(v2);
  rect(xy2.x, xy2.y, 100, 20);
   
}
