class Resources{
  ArrayList<Resource> resourceArr = new ArrayList<Resource>();
  Resources(){}
  
  void addResource(Resource x){
    resourceArr.add(x);
    //print(resourceArr.length);
  }
  
  void displayAll(){
    for (int i = 0; i < resourceArr.size(); i++ ) { 
      resourceArr.get(i).display();
    }
  }
  
  void drainAllHealth(int x, int y){
    for (int i = resourceArr.size() - 1; i >= 0; i--) { 
      resourceArr.get(i).drainHealth(x,y);
      //print (resourceArr.get(i).health, "\n");
      
      if (resourceArr.get(i).health <= 0){
        resourceArr.remove(i);
      }
    }
  }
  
  Resource getNearest(int x, int y){
    if (resourceArr.size() == 0){
      return null;
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
    //print(minDistance);
    return closest;
  }
}
