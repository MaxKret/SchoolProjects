//globals
String path = "C:\\Users\\Crackhead\\Desktop\\College Stuff\\CS324E\\Processing_Labs\\";
PFont courier;
String display_str = "";

//setup
void setup()
{
  surface.setResizable(true);
  size(500, 500);
  background(0);
  courier = createFont("Courier", 32);
  textFont(courier);
}


void draw() 
{
  textAlign(CENTER);
  text("Typewriter", 250, 32);
  textAlign(LEFT);
  text(display_str, 50, 100);
}

void keyTyped()
{
  if((key >= 'A' && key <= 'Z') || (key >= 'a' && key <= 'z'))
  {
    display_str += key;
  }
  if(key == ' ')
  {
    display_str += key;
  }
  if(key == ENTER || key == RETURN || keyCode == 10)
  {
    display_str += '\n';
  }
}
