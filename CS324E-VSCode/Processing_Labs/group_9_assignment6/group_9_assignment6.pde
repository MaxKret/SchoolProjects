Predators predators;
Preys preys;
Resources resources;
PImage img;

void setup() 
{
  size(640, 360);
  img = loadImage("resource.png");
  
  // Add predators
  predators = new Predators();
  for (int i = 0; i < 5; i++) 
  {
    predators.addPredator(new Predator(0 + 30, 0 + 30));
  }
  
  // Add prey
  preys = new Preys();
  for (int i = 0; i < 10; i++) 
  {
    preys.addPrey(new Prey(width - 30,height - 30));
  }
  
  // Add resources
  resources = new Resources();
  
  // let them see eachother 
  predators.addHuntedPrey(preys);
  preys.addHuntingPredators(predators);
  preys.addResources(resources);
  
  
}

void draw() 
{
  background(50);
  predators.run();
  preys.run();
  resources.displayAll();
  
  // saveframe 
  //saveFrame("frames/frame-######.tif");
}

// event handling
void mousePressed(){
  Resource temp = new Resource(mouseX,mouseY,img);
  resources.addResource(temp);
}

void keyPressed()
{
  if (key == 'b') {
    preys.addPrey(new Prey( mouseX, mouseY));
  } else {
    predators.addPredator(new Predator(mouseX, mouseY));
  }
}
