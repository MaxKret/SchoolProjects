class Preys 
{
  ArrayList<Prey> preys; // An ArrayList for all the preys
  Predators huntingPredator;
  Resources ResourceWrapper;

  Preys() 
  {
    preys = new ArrayList<Prey>(); // Initialize the ArrayList
  }

  void run() 
  {
    for (Prey b : preys) 
    {
      b.run(preys, huntingPredator.predators, ResourceWrapper);  // Passing the entire list of preys to each prey individually
    }
  }

  void addPrey(Prey b) 
  {
    preys.add(b);
  }
  
  void addHuntingPredators(Predators _huntingPredator)
  {
    huntingPredator = _huntingPredator;
  }

void addResources(Resources ResourceWrapper){
  this.ResourceWrapper = ResourceWrapper;
}
}
