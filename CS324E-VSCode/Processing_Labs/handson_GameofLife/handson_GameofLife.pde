int size = 75; // MAXIMUM 75 WITHOUT REDUCING TEXT SIZE
String gridText;
int[] currentGrid = new int[size];
int[] previousGrid = new int[size];


//Underpopulation: Any "alive" cell with 0 neighbors will die
//Stable population: Any "alive" cell with 1 neighbors will survive
//Overpopulation: Any "alive" cell with 2 neighbors will die
//Reproduction: Any "dead" cell with exactly 1 neighbors will be born



void setup()
{
  size(1200,400);
  frameRate(1);
  // setup and print initial grid
  currentGrid[4] = 1;
  currentGrid[5] = 1;
  currentGrid[7] = 1;
  arrayCopy(currentGrid, previousGrid);
  gridText = printGrid();
}

void draw()
{
  // print current grid
  background(210);
  textSize(25);
  textAlign(CENTER,CENTER);
  text(gridText,width/2,height/2);
  
  // use previous to alter current grid  
  updateGrid();
  
  
  // update grid text w/ currentGrid and previous w/ current
  gridText = printGrid(); //<>//
  arrayCopy(currentGrid, previousGrid);
}

void updateGrid()
{
  for(int i=0;i<size;i++)
  {
    updateCell(i);
  }
}

void updateCell(int idx)
{
  int nNbrs = numNeighbors(idx);
  //dead cell
  if(previousGrid[idx] == 0)
  {
    if(nNbrs == 1)// 1 nbr
    {
      currentGrid[idx] = 1;// come alive
    }
    //else stay dead
  }
  //alive cell
  else
  {
    if(nNbrs != 1)// 0 or 2 nbrs
    {
      currentGrid[idx] = 0;// die
    }
    //else stay alive
  }
  
}

int numNeighbors(int idx)
{
  int nNeighbors = 0;
  if(idx == 0)//no left nbr
  {
    nNeighbors = previousGrid[idx+1];
  }
  else if(idx == size-1) // no right nbr
  {
    nNeighbors = previousGrid[idx-1];
  }
  else
  {
    nNeighbors = previousGrid[idx-1] + previousGrid[idx+1];
  }
  return nNeighbors;
}


String printGrid()
{
  String res = "";
  res += "[";
  for(int i=0;i<size;i++)
  {
    res += currentGrid[i];
  }
  res += "]";
  println(res);
  return res;
}
