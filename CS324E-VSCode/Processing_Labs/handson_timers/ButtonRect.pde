class ButtonRect extends Button
{
  int x,y,w,h;
  
  ButtonRect(int _x, int _y, int _w, int _h, color _hovered, color _unselected)
  {
    super(_hovered,_unselected);
    x = _x;
    y = _y;
    w = _w;
    h = _h;
  }
  
  void update()
  {
    if(mouseX>x && mouseX<x+w && mouseY>y && mouseY<y+h) isMouseOver = true;
    else isMouseOver = false;
  }
  
  void drawButton()
  {
    rect(x,y,w,h);
  }
}
