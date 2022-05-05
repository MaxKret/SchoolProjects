class ButtonCheckbox extends Button
{
  int x,y,w,h;
  int id;
  boolean on_state = false;
  color selected;
  
  ButtonCheckbox(int _x, int _y, int _w, int _h, int _id,
                 color _hovered, color _unselected, color _selected)
  {
    super(_hovered,_unselected);
    selected = _selected;
    x = _x;
    y = _y;
    w = _w;
    h = _h;
    id = _id;
  }
  
  void display()
  {
    if(isMouseOver) fill(hovered);
    else if(on_state) fill(selected);
    else fill(unselected);
    drawButton();
  }
  
  void update()
  {
    if(mouseX>x && mouseX<x+w && mouseY>y && mouseY<y+h) isMouseOver = true;
    else isMouseOver = false;
  }
  
  void switchState()
  {
    on_state = !on_state;
    if(on_state) println("Checkbox "+id+" at ("+x+","+y+") is on");
    else println("Checkbox "+id+" at ("+x+","+y+") is off");
  }
  
  void mousePressed()
  {
    if(isPressed())
    {
      switchState();
    }
  }
  
  void drawButton()
  {
    rect(x,y,w,h);
  }
}
