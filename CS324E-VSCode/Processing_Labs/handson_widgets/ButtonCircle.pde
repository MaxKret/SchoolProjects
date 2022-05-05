class ButtonCircle extends Button
{
  int x,y,r;
  
  ButtonCircle(int _x, int _y, int _r, color _hovered, color _unselected)
  {
    super(_hovered,_unselected);
    x = _x;
    y = _y;
    r = _r;
  }
  
  void update()
  {
    if(dist(mouseX,mouseY,x,y) <= r) isMouseOver = true;
    else isMouseOver = false;
  }
  
  void drawButton()
  {
    ellipse(x,y,r*2,r*2);
  }
}
