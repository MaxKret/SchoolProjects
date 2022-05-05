Predators predators;
Preys preys;
Resources resourceList;
PImage img;

void setup() 
{
  size(640, 360);
  img = loadImage("resource.png");
  resourceList = new Resources();
  preys = new Preys();
  preys.addResources(resourceList);
  // Add predators
  predators = new Predators();
  for (int i = 0; i < 5; i++) 
  {
    predators.addPredator(new Predator(0 + 30, 0 + 30));
  }
  
  for (int i = 0; i < 10; i++) 
  {
    preys.addPrey(new Prey(width - 30,height - 30));
  }
  
  // let them see eachother 
  predators.addHuntedPrey(preys);
  preys.addHuntingPredators(predators);
}

void draw() 
{
  background(50);
  predators.run();
  preys.run();
  resourceList.displayAll();
}

void mousePressed(){
  Resource temp = new Resource(mouseX,mouseY,img);
  resourceList.addResource(temp);
}

// Add a new predator into the System
void keyPressed() 
{
  predators.addPredator(new Predator(mouseX,mouseY));
}
