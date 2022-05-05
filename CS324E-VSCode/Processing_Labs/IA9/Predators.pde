class Predators 
{
  ArrayList<Predator> predators; // An ArrayList for all the predators
  Preys huntedPrey;

  Predators() 
  {
    predators = new ArrayList<Predator>(); // Initialize the ArrayList
  }

  void run() 
  {
    for (Predator b : predators) 
    {
      b.run(predators, huntedPrey.preys);  // Passing the entire list of predators to each predator individually
    }
  }

  void addPredator(Predator b) 
  {
    predators.add(b);
  }
  
  void addHuntedPrey(Preys _huntedPrey)
  {
    huntedPrey = _huntedPrey;
  }
}
