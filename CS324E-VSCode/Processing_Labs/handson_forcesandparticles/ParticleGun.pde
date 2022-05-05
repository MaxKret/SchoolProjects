class ParticleGun
{
  float x, y;
  Particle[] particles;
  
  Particle a,b,c;
  
  ParticleGun() 
  {
    x = width/2-55;
    y = height - 100;
    
    a = new Particle(x+70,y,0,0,10);
    b = new Particle(x+35,y,0,0,10);
    c = new Particle(x,y,0,0,10);
    
    particles = new Particle[3];
    particles[0] = a;
    particles[1] = b;
    particles[2] = c;
  }
  
  void applyForces() 
  {
    for(int i = 0; i < 3; i++)
    {
      if(particles[i].x >= width || particles[i].y >= height) //<>//
      {
        //reset
        particles[i].x = x;
        particles[i].y = y;
        particles[i].vx = 0;
        particles[i].vy = 0;
      }
      if( particles[i].x < x+80 ) particles[i].applyForces(.7, 0);
      else particles[i].applyForces(.7, 9.8/62.5);
    }
  }
  
  void display() 
  {
    fill(255,0,0);
    a.display();
    fill(0,255,0);
    b.display();
    fill(0,0,255);
    c.display();
    pushMatrix();
    translate(x,y);
    fill(255);
    rect(-10,-15,80,30);
    popMatrix();
  }
}
