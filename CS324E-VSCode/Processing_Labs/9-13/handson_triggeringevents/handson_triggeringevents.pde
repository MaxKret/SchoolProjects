void setup()
{
  size(500,500);
}

void draw()
{
  // background
  if (mousePressed) 
  {
    if (mouseButton == LEFT) 
    {
      background(0);
    }
    else if(mouseButton == RIGHT)
    {
      background(255);
    }
    else
    {
      background(100);
    }
  }
  
  // letters
  if (keyPressed && ((key >= 'A' && key <= 'Z') || (key >= 'a' && key <= 'z')))
  {
    text(key, mouseX, mouseY);
  }
}

void mousePressed()
{
  if (mouseButton == LEFT) 
    {
      background(0);
    }
    else if(mouseButton == RIGHT)
    {
      background(255);
    }
    else
    {
      background(100);
    }
}

void mouseMoved()
{
  fill(110);
  stroke(110);
  ellipse(mouseX, mouseY, 1, 1);
}

void keyPressed()
{
  if((key >= 'A' && key <= 'Z') || (key >= 'a' && key <= 'z'))
  {
    text(key, mouseX, mouseY);
  }
}
