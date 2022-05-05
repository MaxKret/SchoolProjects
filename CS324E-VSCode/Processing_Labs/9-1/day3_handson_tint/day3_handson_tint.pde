//globals
String path = "C:\\Users\\Crackhead\\Desktop\\College Stuff\\CS324E\\Processing_Labs\\";
PImage imgIn;
 
 
//setup
void setup()
 {
   imgIn = loadImage(path+"test.jpg");
   surface.setResizable(true);
   surface.setSize((imgIn.width), (imgIn.height));
   background(255);
 }
 
 
//draw
void draw()
 {
//reset stroke and fill
   noStroke();
   noFill();
   
   image(imgIn,0,0);
   myTint(imgIn,255,0,0);
   
//reset stroke and fill
   noStroke();
   noFill();
 }

//myTint()
void myTint(PImage input, float R, float G, float B)
{
  loadPixels();
  input.loadPixels();
  for (int y = 0; y < height; y++) 
  {
    for (int x = 0; x < width; x++) 
    {
      int loc = x + y*width;
      
      float r = red(input.pixels[loc])+R;
      float g = green(input.pixels[loc])+G;
      float b = blue(input.pixels[loc])+B;
      
      pixels[loc] =  color(r,g,b);
    }
  }
  updatePixels();
  noFill();
  
}
