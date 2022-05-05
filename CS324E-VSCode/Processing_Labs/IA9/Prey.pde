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

      // This is a new PVector method not yet implemented in JS
      // velocity = PVector.random2D();

      // Leaving the code temporarily this way so that this example runs in JS
    float angle = random(TWO_PI);
    velocity = new PVector(cos(angle), sin(angle));

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
    // We could add mass here if we want A = F / M
    acceleration.add(force);
  }

  // We accumulate a new acceleration each time based on three rules
  void flock(ArrayList<Prey> preys, ArrayList<Predator> predators, Resources ResourcesWrapper)
  {
    PVector sep = separate(preys);   // Separation
    PVector ali = align(preys);      // Alignment
    PVector coh = cohesion(preys);   // Cohesion
    PVector run = runaway(predators);   // Cohesion
    PVector hunt = resourceHunt(ResourcesWrapper);
    // Arbitrarily weight these forces
    sep.mult(1.5); // 1.5
    ali.mult(1.0);
    coh.mult(1.0);
    run.mult(1.0);
    // Add the force vectors to acceleration
    applyForce(sep);
    applyForce(ali);
    applyForce(coh);
    applyForce(run);
    applyForce(hunt);
  }

  // Method to update position
  void update() {
    // Update velocity
    velocity.add(acceleration );
    // Limit speed
    velocity.limit(maxspeed * multiplier);
    position.add(velocity);
    // Reset accelertion to 0 each cycle
    acceleration.mult(0);
  }

  // A method that calculates and applies a steering force towards a target
  // STEER = DESIRED MINUS VELOCITY
  PVector seek(PVector target) {
    PVector desired = PVector.sub(target, position);  // A vector pointing from the position to the target
    // Scale to maximum speed
    desired.setMag(maxspeed  * multiplier);
    // Steering = Desired minus Velocity
    PVector steer = PVector.sub(desired, velocity);
    steer.limit(maxforce  * multiplier);  // Limit to maximum steering force
    return steer;
  }

  void render() {
    // Draw a triangle rotated in the direction of velocity
    float theta = velocity.heading() + radians(90); // arrow pointing down so offset right

    stroke(255);
    pushMatrix();
    translate(position.x, position.y);
    fill(0);
    line(0, 0, velocity.x*10, velocity.y*10);
    shape(antelShape);
    rotate(theta);
    fill(200, 100);
    beginShape(TRIANGLES);
    vertex(0, -r*2);
    vertex(-r, r*2);
    vertex(r, r*2);
    endShape();
    popMatrix();
  }

  void borders() {
    // wrap-around
    //if (position.x < -r) position.x = width+r;
    //if (position.y < -r) position.y = height+r;
    //if (position.x > width+r) position.x = -r;
    //if (position.y > height+r) position.y = -r;

    // bounce
    if ((position.x < 0) || (position.x > width)) velocity.x *= -1;
    if ((position.y < 0) || (position.y > height)) velocity.y *= -1;
  }

  // Separation
  // Method checks for nearby preys and steers away
  PVector separate (ArrayList<Prey> preys)
  {
    PVector steer = new PVector(0, 0, 0);
    int count = 0;
    // For every prey in the system, check if it's too close
    for (Prey other : preys) {
      float d = PVector.dist(position, other.position);
      // If the distance is greater than 0 and less than an arbitrary amount (0 when you are yourself)
      if ((d > 0) && (d < 25)) {
        // Calculate vector pointing away from neighbor
        PVector diff = PVector.sub(position, other.position);
        diff.normalize();
        diff.div(d);        // Weight by distance
        steer.add(diff);
        count++;            // Keep track of how many
      }
    }
    // Average -- divide by how many
    if (count > 0) {
      steer.div((float)count);
    }

    // As long as the vector is greater than 0
    if (steer.mag() > 0) {
      // Implement Reynolds: Steering = Desired - Velocity
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
    // For every prey in the system, check if it's too close
    for (Predator other : predators) {
      float d = PVector.dist(position, other.position);
      // If the distance is greater than 0 and less than an arbitrary amount (0 when you are yourself)
      if ((d > 0) && (d < desiredseparation)) {
        // Calculate vector pointing away from neighbor
        PVector diff = PVector.sub(position, other.position);
        diff.normalize();
        diff.div(d);        // Weight by distance
        steer.add(diff);
        count++;            // Keep track of how many
      }
    }
    // Average -- divide by how many
    if (count > 0) {
      steer.div((float)count);
    }

    // As long as the vector is greater than 0
    if (steer.mag() > 0) {
      // Implement Reynolds: Steering = Desired - Velocity
      steer.setMag(maxspeed);
      steer.sub(velocity);
      steer.limit(maxforce);
    }
    return steer;
  }

  // Alignment
  // For every nearby prey in the system, calculate the average velocity
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
      // Implement Reynolds: Steering = Desired - Velocity
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
  // For the average position (i.e. center) of all nearby preys, calculate steering vector away from that position
  PVector cohesion (ArrayList<Prey> preys) {
    float neighbordist = 90;
    PVector sum = new PVector(0, 0);   // Start with empty vector to accumulate all positions
    int count = 0;
    for (Prey other : preys) {
      float d = PVector.dist(position, other.position);
      if ((d > 0) && (d < neighbordist)) {
        sum.add(other.position); // Add position
        count++;
      }
    }
    if (count > 0) {
      sum.div(count);
      return seek(sum);  // Steer towards the position
    } else {
      return new PVector(0, 0);
    }
  }
}
