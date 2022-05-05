import java.util.*;
class Predator 
{

  PVector position;
  PVector velocity;
  PVector acceleration;
  float r;
  float maxforce;    // Maximum steering force
  float maxspeed;    // Maximum speed
  float desiredseparation;

  PShape lionShape;

  Predator(float x, float y) 
  {
    acceleration = new PVector(0, 0);
    velocity = PVector.random2D();
    position = new PVector(x, y);
    r = 2.0;
    maxspeed = 1.0; // 2.0
    maxforce = 0.03;

    lionShape = loadShape("lion.svg");
    lionShape.scale(0.1);
  }

  void run(ArrayList<Predator> predators, ArrayList<Prey> preys) 
  {
    flock(predators, preys);
    update();
    borders();
    render();
  }

  void applyForce(PVector force) 
  {
    acceleration.add(force);
  }

  void flock(ArrayList<Predator> predators, ArrayList<Prey> preys) 
  {
    PVector sep = separate(predators);   // Separation : average pos of all close nbrs
    PVector hunt = hunting(preys);   // Incohesion : average pos of all close neighbors
    sep.mult(2.0); // 1.5
    hunt.mult(1.0); // 1.0

    applyForce(sep);
    applyForce(hunt);
  }

  void update() 
  {
    // Update velocity
    velocity.add(acceleration);
    // Limit speed
    velocity.limit(maxspeed);
    position.add(velocity);
    // Reset accelertion
    acceleration.mult(0);
  }

  //Reynolds: STEER = DESIRED MINUS VELOCITY
  PVector seek(PVector target) 
  {
    PVector desired = PVector.sub(target, position);
    desired.setMag(maxspeed);

    //Reynolds: Steering = Desired minus Velocity
    PVector steer = PVector.sub(desired, velocity);
    steer.limit(maxforce);
    return steer;
  }

  void render() 
  {
    // Draw a triangle rotated in the direction of velocity
    float theta = velocity.heading() + radians(90);


    stroke(255);
    pushMatrix();
    translate(position.x, position.y);
    fill(0);
    line(0, 0, velocity.x*10, velocity.y*10);
    shape(lionShape);
    rotate(theta);
    fill(200, 100);
    // velocity indicator
    beginShape(TRIANGLES);
    vertex(0, -r*2);
    vertex(-r, r*2);
    vertex(r, r*2);
    endShape();
    popMatrix();
  }

  void borders() 
  {
    if ((position.x < 0) || (position.x > width)) velocity.x *= -1;
    if ((position.y < 0) || (position.y > height)) velocity.y *= -1;
  }

  // Separation
  PVector separate (ArrayList<Predator> predators) 
  {
    desiredseparation = 100.0f; // 25.0
    PVector steer = new PVector(0, 0, 0);
    int count = 0;
    for (Predator other : predators) 
    {
      float d = PVector.dist(position, other.position);
      if ((d > 0) && (d < desiredseparation)) 
      {
        PVector diff = PVector.sub(position, other.position);
        diff.normalize();
        diff.div(d);       
        steer.add(diff);
        count++;          
      }
    }
    if (count > 0) 
    {
      steer.div((float)count);
    }

    if (steer.mag() > 0) 
    {
      // Reynolds: Steering = Desired - Velocity
      steer.setMag(maxspeed);
      steer.sub(velocity);
      steer.limit(maxforce);
    }
    return steer;
  }

  // Hunting
  PVector hunting (ArrayList<Prey> preys) 
  {
    float closedist = 250f;
    PVector sum = new PVector(0, 0); 
    int count = 0;
    for (Prey prey : preys) 
    {
      float d = PVector.dist(position, prey.position);
      if ((d > 0) && (d < closedist))
      {
        sum.add(prey.position);
        count++;
      }
    }
    if (count > 0) 
    {
      sum.div(count);
      return seek(sum);
    } else 
    {
      return new PVector(0, 0);
    }
  }
  
  
  ArrayList<Predator> getNearestPredator(ArrayList<Predator> predators, PVector pos) 
  {/* returns res*/
    float limit = 600;
    ArrayList<Predator> res = new ArrayList<Predator>();
    float minDist = 9e9;
    
    for (Predator other : predators) 
    {
      float d = PVector.dist(pos, other.position);
      if ((d > 0) && (d < limit) && (d < minDist)) 
      {
        minDist = d;
        res.add(0,other);
      }
    }
    return res;
  }
}
