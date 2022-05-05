// globals
Button rButton1,rButton2,cButton1,cButton2;
float background_greyscale;

// setup
void setup()
{
  size(500,500);
              //"rect" or "circ", X,  Y,  r
  rButton1 = new Button("rect", 100, 50, 10);
  rButton2 = new Button("rect", 140, 50, 20);
  cButton1 = new Button("circ", 180, 50, 10);
  cButton2 = new Button("circ", 220, 50, 20);
  
  background_greyscale = 250;
}

// draw
void draw()
{
  background(background_greyscale);
  
  rButton1.display();
  rButton2.display();
  cButton1.display();
  cButton2.display();
  
  
}

// event handling
void mousePressed()
{
  rButton1.mousePressed();
  rButton2.mousePressed();
  cButton1.mousePressed();
  cButton2.mousePressed();
}

void mouseReleased()
{
  background_greyscale = 250;
}
