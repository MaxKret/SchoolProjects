class Prey
{

  PVector position;
  PVector velocity;
  PVector acceleration;
  float r;
  float maxforce;    // Maximum steering force
  float maxspeed;    // Maximum speed
  float desiredseparation;
  float satisfaction;
  float multiplier;

  PShape antelShape;

  Prey(float x, float y)
  {
    satisfaction = 100;
    acceleration = new PVector(0, 0);
    multiplier = 1;
    desiredseparation = 125.0f;
    
    velocity = PVector.random2D();

    position = new PVector(x, y);
    r = 2.0;
    maxspeed = 2;
    maxforce = 0.03;

    antelShape = loadShape("antelope.svg");
    antelShape.scale(0.02);
  }

  void eat(Resources ResourcesWrapper) {
    
    Resource nearest = ResourcesWrapper.getNearest(position.x, position.y);
    boolean eaten = nearest.drainHealth(position.x, position.y);
    if (eaten) {
      satisfaction += .1;
    } else {
      if (satisfaction <= .2) {
        satisfaction = -.2 ;
      }
    }
    desiredseparation = 5 + satisfaction;
    multiplier = satisfaction/100;
  }

  void run(ArrayList<Prey> preys, ArrayList<Predator> predators, Resources ResourcesWrapper)
  {
    eat(ResourcesWrapper);
    flock(preys, predators, ResourcesWrapper);
    update();
    borders();
    render();

  }

  void applyForce(PVector force)
  {
    acceleration.add(force);
  }

  void flock(ArrayList<Prey> preys, ArrayList<Predator> predators, Resources ResourcesWrapper)
  {
    PVector sep = separate(preys);
    PVector ali = align(preys);
    PVector coh = cohesion(preys);
    PVector run = runaway(predators);  
    PVector hunt = resourceHunt(ResourcesWrapper);
    
    sep.mult(1.5); // 1.5
    ali.mult(1.0);
    coh.mult(1.0);
    run.mult(1.0);
    
    applyForce(sep);
    applyForce(ali);
    applyForce(coh);
    applyForce(run);
    applyForce(hunt);
  }

  void update() {
    // Update velocity
    velocity.add(acceleration );
    // Limit speed
    velocity.limit(maxspeed * multiplier);
    position.add(velocity);
    // Reset accelertion
    acceleration.mult(0);
  }

  //Reynolds: STEER = DESIRED MINUS VELOCITY
  PVector seek(PVector target) {
    PVector desired = PVector.sub(target, position);
    // Scale to maximum speed
    desired.setMag(maxspeed  * multiplier);
    PVector steer = PVector.sub(desired, velocity);
    steer.limit(maxforce  * multiplier);
    return steer;
  }

  void render() {
    float theta = velocity.heading() + radians(90); // arrow pointing down so offset right

    stroke(255);
    pushMatrix();
    translate(position.x, position.y);
    fill(0);
    line(0, 0, velocity.x*10, velocity.y*10);
    shape(antelShape);
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

  void borders() {
    // bounce
    if ((position.x < 0) || (position.x > width)) velocity.x *= -1;
    if ((position.y < 0) || (position.y > height)) velocity.y *= -1;
  }

  // Separation
  PVector separate (ArrayList<Prey> preys)
  {
    PVector steer = new PVector(0, 0, 0);
    int count = 0;
    for (Prey other : preys) {
      float d = PVector.dist(position, other.position);
      if ((d > 0) && (d < 25)) {
        PVector diff = PVector.sub(position, other.position);
        diff.normalize();
        diff.div(d);        
        steer.add(diff);
        count++;           
      }
    }
    if (count > 0) {
      steer.div((float)count);
    }

    if (steer.mag() > 0) {
      //Reynolds: Steering = Desired - Velocity
      steer.setMag(maxspeed);
      steer.sub(velocity);
      steer.limit(maxforce);
    }
    return steer;
  }

  PVector runaway(ArrayList<Predator> predators)
  { // 25.0
    PVector steer = new PVector(0, 0, 0);
    int count = 0;
    for (Predator other : predators) {
      float d = PVector.dist(position, other.position);
      if ((d > 0) && (d < desiredseparation)) {
        PVector diff = PVector.sub(position, other.position);
        diff.normalize();
        diff.div(d);        
        steer.add(diff);
        count++;           
      }
    }
    if (count > 0) {
      steer.div((float)count);
    }

    if (steer.mag() > 0) {
      // Reynolds: Steering = Desired - Velocity
      steer.setMag(maxspeed);
      steer.sub(velocity);
      steer.limit(maxforce);
    }
    return steer;
  }

  // Alignment
  PVector align (ArrayList<Prey> preys) {
    float neighbordist = 50;
    PVector sum = new PVector(0, 0);
    int count = 0;
    for (Prey other : preys) {
      float d = PVector.dist(position, other.position);
      if ((d > 0) && (d < neighbordist)) {
        sum.add(other.velocity);
        count++;
      }
    }
    if (count > 0) {
      sum.div((float)count);
      // reynolds: Steering = Desired - Velocity
      sum.setMag(maxspeed);
      PVector steer = PVector.sub(sum, velocity);
      steer.limit(maxforce);
      return steer;
    } else {
      return new PVector(0, 0);
    }
  }


  PVector resourceHunt(Resources ResourceWrapper) {
    Resource nearest = ResourceWrapper.getNearest(position.x, position.y);
    PVector location = new PVector(nearest.xLoc, nearest.yLoc);
    float dist = PVector.dist(location, position);
    if (dist < 325 - satisfaction * 2) {
      return seek(location);
    }
    return new PVector(0, 0);
  }

  // cohesion
  PVector cohesion (ArrayList<Prey> preys) {
    float neighbordist = 90;
    PVector sum = new PVector(0, 0); 
    int count = 0;
    for (Prey other : preys) {
      float d = PVector.dist(position, other.position);
      if ((d > 0) && (d < neighbordist)) {
        sum.add(other.position);
        count++;
      }
    }
    if (count > 0) {
      sum.div(count);
      return seek(sum);
    } else {
      return new PVector(0, 0);
    }
  }
}
