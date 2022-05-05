PImage imgIn;
PImage imgOut;
String path = "C:\\Users\\Crackhead\\Desktop\\College Stuff\\CS324E\\Processing_Labs\\";


void setup()
{
  background(255);
  surface.setResizable(true);

  imgIn = loadImage(path+"test.jpg");
  imgOut = createImage(imgIn.width, imgIn.height, ARGB);
  imgOut.copy(imgIn, 0, 0, imgIn.width, imgIn.height, 0, 0, imgOut.width, imgOut.height);
  surface.setSize(imgIn.width*2, imgIn.height);
}

void draw()
{
  image(imgIn, 0, 0);
  image(imgOut, imgIn.width, 0);

  mySharpen(imgIn, imgOut);
}

void mySharpen(PImage input, PImage output)
{
  float[][] matrix = {{0, -1, 0}, {-1, 5, -1}, {0, -1, 0}};


  // traverse pixels
  for (int y = 1; y < input.height-1; y++) 
  {
    for (int x = 1; x < input.width-1; x++) 
    {
      // each pixel:
      int loc = x + y*input.width;
      float r = 0;
      float g = 0;
      float b = 0;

      // traverse neighbors
      for (int i = 0; i < 3; i++) 
      {
        for (int j = 0; j < 3; j++) 
        {
          // each neighbor pixel(including center)
          int index = (x + i - 1) + input.width*(y + j - 1);
          r += red(input.pixels[index]) * matrix[i][j];
          g += green(input.pixels[index]) * matrix[i][j];
          b += blue(input.pixels[index]) * matrix[i][j];
        }
      }
      // end traverse neighbors

      // send rgb to output
      r = constrain(abs(r), 0, 255);
      g = constrain(abs(g), 0, 255);
      b = constrain(abs(b), 0, 255);
      output.pixels[loc] =  color(r, g, b);
    }
  }
  output.updatePixels();
}
