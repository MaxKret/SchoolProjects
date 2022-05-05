class Particle 
{
  //Class fields
  PVector xy,v,a;
  float m;
  float r;
  
  Particle(float _x, float _y, float _vx, float _vy, float _m, float _r) 
  {
    xy = new PVector(_x,_y);
    v = new PVector(_vx,_vy);
    a = new PVector(0,0);
    m = _m;
    r = _r;
  }
  void applyForces(float _fx, float _fy) 
  {
    PVector f = new PVector(_fx,_fy);
    a = f.div(m);
    v.add(a);
    xy.add(v);

  }
  void display() 
  {
    ellipse(xy.x, xy.y, r, r);
  }
}
