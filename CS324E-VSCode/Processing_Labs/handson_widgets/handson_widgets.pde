// globals
float background_greyscale;
boolean circlePressed,rectPressed = false;

ButtonCircle circle1;
ButtonRect rect1;
ButtonCheckbox checkbox1,checkbox2;
ButtonSlider slider1;
RadioButtons radio1;

// setup
void setup()
{
  size(500,500);
  
  circle1 = new ButtonCircle(75, 130, 30, color(110), color(25));
  rect1 = new ButtonRect(200, 100, 80, 60, color(110), color(255));
  checkbox1 = new ButtonCheckbox(350, 100, 25, 25, 4, color(110), color(255), color(0));
  checkbox2 = new ButtonCheckbox(350, 135, 25, 25, 5, color(110), color(255), color(0));
  slider1 = new ButtonSlider(200, 250, 200, 30, color(110), color(255));
  radio1 = new RadioButtons(60, 200, 25, 25, 4, 1, color(110), color(255), color(0));
  //                      // x,   y,  w,  h,nBts, id, hovered, unselected, selected
  
  background_greyscale = 220;
}

// draw
void draw()
{
  
  background(background_greyscale);
  
  
  
  circle1.update();
  rect1.update();
  checkbox1.update();
  checkbox2.update();
  slider1.update();
  radio1.update();
  
  if(circlePressed) background(0);
  else if(rectPressed) background(255);
  else background(background_greyscale);
  
  circle1.display();
  rect1.display();
  checkbox1.display();
  checkbox2.display();
  slider1.display();
  radio1.display();

}

// event handling
void mousePressed()
{
  if(circle1.isPressed()) circlePressed = !circlePressed;
  if(rect1.isPressed()) rectPressed = !rectPressed;
  checkbox1.mousePressed();
  checkbox2.mousePressed();
  slider1.mousePressed();
  radio1.mousePressed();
}

void mouseReleased()
{
  circle1.isReleased();
  rect1.isReleased();
}
