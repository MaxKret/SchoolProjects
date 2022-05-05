class Button
{
  boolean isMouseOver,isMousePressed;
  color hovered, unselected;
  
  Button(color _hovered, color _unselected)
  {
   hovered = _hovered;
   unselected = _unselected;
   isMouseOver = isMousePressed = false;
  }
  
  void display()
  {
    if(isMouseOver) fill(hovered);
    else fill(unselected);
    drawButton();
  }
  
  void drawButton()
  {}
  
  boolean isPressed()
  {
    if(isMouseOver)
    {
      isMousePressed = true;
      return true;
    }
    return false;
  }
  
  boolean isReleased()
  {
    isMousePressed = false;
    return false;
  }
  
}
