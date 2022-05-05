class Tree 
{
  //properties/fields
  color TreeBrown = color(#381d10);
  PShape trunk;
  PShape b1;
  PShape b2;
  PShape b3;
  PShape treeBranch;
  PShape branch;
  float x, y;
  float blossomX,blossomY;
  float shakeSpeed;
  float branchAngle;
  float swaySpeed;
  float trunkAngle;


  //constructors
  Tree()
  {
    this.x = 10;
    this.y = 140;
    branchAngle = 0;
    shakeSpeed = 0.25;
    trunkAngle = 0;
    swaySpeed = 0.01;

    fill(TreeBrown);
    noStroke();
    trunk = createShape(RECT, 0, 0, 50, 400);
    stroke(0);
    noFill();
    
    pushMatrix();
    treeBranch = loadShape("treeBranchSVG.svg");
    treeBranch.scale(0.095);
    popMatrix();
    
    fill(228,146,231);
    
    pushMatrix();
    b1 = createShape();
    b1.translate(46,50);
    b1.rotate(radians(50));
    b1.beginShape();
    b1.vertex(0,0); 
    b1.vertex(-5,10); 
    b1.vertex(3,20); 
    b1.vertex(10,25); 
    b1.vertex(15,26); 
    b1.vertex(12,10); 
    b1.vertex(0,0); 
    b1.endShape();
    popMatrix();
    
    pushMatrix();
    b2 = createShape();
    b2.translate(52,90);
    b2.rotate(radians(20));
    b2.beginShape();
    b2.vertex(0,0); 
    b2.vertex(-5,10); 
    b2.vertex(3,20); 
    b2.vertex(10,25); 
    b2.vertex(15,26); 
    b2.vertex(12,10); 
    b2.vertex(0,0); 
    b2.endShape();
    popMatrix();
    
    pushMatrix();
    b3 = createShape();
    b3.translate(76,95);
    b3.rotate(radians(30));
    b3.beginShape();
    b3.vertex(0,0); 
    b3.vertex(-5,10); 
    b3.vertex(3,20); 
    b3.vertex(10,25); 
    b3.vertex(15,26); 
    b3.vertex(12,10); 
    b3.vertex(0,0); 
    b3.endShape();
    popMatrix();
    
    fill(255);
    
    branch = createShape(GROUP);
    branch.addChild(treeBranch);
    branch.addChild(b1);
    branch.addChild(b2);
    branch.addChild(b3);
    
  }



  //methods
  void display()
  {
  }


  void move()
  {
    moveBranches();
    moveTrunk();
  }

  void moveBranches()
  {
    pushMatrix();
    translate(this.x+40, this.y+5);
    pushMatrix();
    rotate(radians(5) + radians(branchAngle));
    shape(branch);
    popMatrix();
    popMatrix();

    pushMatrix();
    translate(this.x+37, this.y+7);
    pushMatrix();
    rotate(radians(-50) + radians(-branchAngle));
    shape(branch);
    popMatrix();
    popMatrix();

    pushMatrix();
    translate(this.x+35, this.y+10);
    pushMatrix();
    rotate(radians(-100) + radians(branchAngle));
    shape(branch);
    popMatrix();
    popMatrix();
    
    pushMatrix();
    translate(this.x+33, this.y+10);
    pushMatrix();
    rotate(radians(-140) + radians(-branchAngle));
    shape(branch);
    popMatrix();
    popMatrix();
    
    pushMatrix();
    translate(this.x+28, this.y+10);
    pushMatrix();
    rotate(radians(-175) + radians(branchAngle));
    shape(branch);
    popMatrix();
    popMatrix();
    
    pushMatrix();
    translate(this.x+20, this.y+15);
    pushMatrix();
    rotate(radians(-220) + radians(-branchAngle));
    shape(branch);
    popMatrix();
    popMatrix();

    branchAngle += shakeSpeed;
    if (abs(branchAngle) > 10)
    {
      shakeSpeed *= -1;
    }
  }
  
  void moveTrunk()
  {
    pushMatrix();
    translate(this.x+(trunk.width/2), this.y+(trunk.height/2));
    pushMatrix();
    rotate(radians(trunkAngle));
    shape(trunk);
    popMatrix();
    popMatrix();
    trunkAngle += swaySpeed;
    if (trunkAngle > 1.5 || trunkAngle <= 0)
    {
      swaySpeed *= -1;
    }
  }

  void set_shakeSpeed(float new_speed)
  {
    this.shakeSpeed = new_speed;
  }
}
