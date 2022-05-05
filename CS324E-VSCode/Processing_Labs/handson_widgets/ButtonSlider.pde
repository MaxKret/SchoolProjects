class ButtonSlider extends Button
{
  int x,y,w,h;
  float slider_val;
  float prog_percent;
  
  ButtonSlider(int _x, int _y, int _w, int _h, color _hovered, color _unselected)
  {
    super(_hovered,_unselected); // unused
    x = _x;
    y = _y;
    w = _w;
    h = _h;
  }
  
  void mousePressed()
  {
    if(isPressed())
    {
      prog_percent = float(mouseX-this.x)/float(w); //<>//
      slider_val = lerp(0,255,prog_percent); //<>//
      background_greyscale = slider_val; //<>//
    }
  }
  
  void update()
  {
    if(mouseX>x && mouseX<x+w && mouseY>y && mouseY<y+h) isMouseOver = true;
    else isMouseOver = false;
  }
  
  void display()
  {
    fill(slider_val+10);
    stroke(125);
    drawButton();
    stroke(0);
  }
  
  void drawButton()
  {
    rect(x,y,w,h);
    rect(x,y,prog_percent*w,h);
  }
}
