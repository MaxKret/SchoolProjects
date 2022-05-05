class Button
{
  // fields
  String shape;
  PShape pShape;
  float centerX, centerY, r;

  // constructor
  Button(String _shape, float _centerX, float _centerY, float _r)
  {
    this.shape = _shape;
    this.centerX = _centerX;
    this.centerY = _centerY;
    this.r = _r;
    if (shape.toLowerCase() == "rect")
    {
      rectMode(RADIUS);
      fill(centerX);
      pShape = createShape(RECT, 0, 0, r, r);
      rectMode(CORNER);//default
    } 
    else if (shape.toLowerCase() == "circ")
    {
      ellipseMode(RADIUS);
      fill(centerX);
      pShape = createShape(ELLIPSE, 0, 0, r, r);
      ellipseMode(CENTER);// default
    }
  }

  // methods
  void display()
  {
    shape(pShape, centerX, centerY);
  }

  void mousePressed()
  {
    if(this.isPressed())
    {
      println(shape+" at ("+centerX+","+centerY+") was pressed"); //<>//
      background_greyscale = centerX;
    }
  }

  boolean isPressed()
  {
    if (this.shape.toLowerCase() == "rect")
    {   
      if(withinRect()) //<>//
      {
        return true; //<>//
      }
    } 
    else if (shape.toLowerCase() == "circ")
    {
      if(withinCirc())
      {
        return true;
      }
    }
    return false;
  }

  boolean withinRect()  
  { //<>//
    if((abs(centerX - mouseX) <= r) && (abs(centerY - mouseY) <= r)) 
    {
      return true; //<>//
    } 
    return false;
  }

  boolean withinCirc() 
  {
    if (sqrt(sq(centerX - mouseX) + sq(centerY - mouseY)) < r ) 
    {
      return true;
    } 
    return false;
  }
  
}
