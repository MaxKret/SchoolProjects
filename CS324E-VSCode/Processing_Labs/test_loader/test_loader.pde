PShape vector;
void setup() 
{
  vector = loadShape("lion.svg");
  vector.scale(0.2);
  size(800,500);
}
void draw() 
{
  
  shape(vector, 100, 100);
  //shape(vector, 200, 200);
}
