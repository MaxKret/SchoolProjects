class Resources{
  ArrayList<Resource> resourceArr = new ArrayList<Resource>();
  Resources(){}
  
  void addResource(Resource x){
    resourceArr.add(x);
  }
  
  void displayAll(){
    for (int i = 0; i < resourceArr.size(); i++ ) { 
      resourceArr.get(i).display();
    }
  }
  
  void drainAllHealth(int x, int y){
    for (int i = resourceArr.size() - 1; i >= 0; i--) { 
      resourceArr.get(i).drainHealth(x,y);
      
      if (resourceArr.get(i).health <= 0){
        resourceArr.remove(i);
      }
    }
  }
  
  Resource getNearest(float x, float y){
    if (resourceArr.size() == 0){
      PImage dumby = loadImage("resource.png");
      Resource returnResource = new Resource(250,250, dumby);
      return returnResource;
    }
    
    float minDistance = sqrt(sq(x-resourceArr.get(0).xLoc) + sq(y-resourceArr.get(0).yLoc));
    Resource closest = resourceArr.get(0);
    for (int i = 0; i < resourceArr.size(); i++ ) { 
      float distance = sqrt(sq(x-resourceArr.get(i).xLoc) + sq(y-resourceArr.get(i).yLoc));
      if (distance < minDistance){
        minDistance = distance;
        closest = resourceArr.get(i);
      }
    }
    return closest;
  }
  
  
}
