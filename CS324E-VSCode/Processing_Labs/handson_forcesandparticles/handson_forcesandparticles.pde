//globals
float p1y,p1r,p1vel,p1accel;
float p2y,p2r,p2vel,p2accel,friction;

Particle p3;
ParticleGun pgun;

//setup
void setup()
{
  size(800,500);
  ellipseMode(RADIUS);
  //p1
  p1y = 30.0;
  p1r = 15.0;
  p1vel = 0.0;
  p1accel = 0.03;
  //p2
  p2y = 30.0;
  p2r = 15.0;
  p2vel = 0.0;
  p2accel = 0.03;
  friction = 0.995;
  //p3
  p3 = new Particle(10,10,0,0,10);
  //pgun
  pgun = new ParticleGun();
  
}

//draw
void draw()
{
  background(255);
  
  // p1 = portal fun
  fill(255);
  ellipse(15, p1y, p1r, p1r);
  p1vel += p1accel;
  p1y += p1vel;
  if (p1y > height) 
  {
    p1y = 0.0;
  }
  
  // p2 = bouncy ball
  fill(255);
  ellipse(45, p2y, p2r, p2r);
  p2vel += p2accel;
  p2vel *= friction;
  p2y += p2vel;
  if (p2y > (height - p2r) )
  {
    p2vel = -p2vel;
  }
  
  // p3 = single Particle
  p3.display();
  p3.applyForces(0.05,0.005);
 
  // pgun
  pgun.display();
  pgun.applyForces();
}
