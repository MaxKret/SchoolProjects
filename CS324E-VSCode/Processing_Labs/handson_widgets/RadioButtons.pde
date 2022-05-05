class RadioButtons extends Button
{
  int x,y,w,h;
  int nBtns;
  int id;
  int id_selected;
  ButtonCheckbox[] contained_btns;
  color selected;
  
  RadioButtons(int _x, int _y, int _w, int _h, int _nBtns, int _id,
                 color _hovered, color _unselected, color _selected)
  {
    super(_hovered,_unselected);
    selected = _selected;
    x = _x;
    y = _y;
    w = _w;
    h = _h;
    nBtns = _nBtns;
    id = _id;
    
    contained_btns = new ButtonCheckbox[nBtns];
    for(int i=0;i<nBtns;i++)
    {
      contained_btns[i] = new ButtonCheckbox(x, y+(i*30), 25, 25, i, _hovered, _unselected, selected);
    }
  }
  
  void display()
  {
    for(int i=0;i<nBtns;i++)
    {
      contained_btns[i].display();
    }
  }
  
  void update()
  {
    for(int i=0;i<nBtns;i++)
    {
      contained_btns[i].update();
    }
  }
  
  void switchStates(int on_id)
  {
    for(int i=0;i<nBtns;i++)
    {
      if(i == on_id) // id to turn on
      {
        contained_btns[i].switchState();
      }
      else // turn off all others
      {
        if(contained_btns[i].on_state) contained_btns[i].on_state = false;
      }
    }
    if(contained_btns[on_id].on_state) println("RadioButtons "+id+" state changed to "+on_id);
    else println("RadioButtons "+id+" state changed to NONE");;
  }
  
  void mousePressed()
  {
    for(int i=0;i<nBtns;i++)
    {
      if(contained_btns[i].isPressed())
      {
        id_selected = i;
        switchStates(id_selected);
      }
    }
    
  }
  
  void drawButton()
  {
    for(int i=0;i<nBtns;i++)
    {
      contained_btns[i].drawButton();
    }
  }
}
