/*
Max K
9/14/21
*/

PImage original_img;
PImage display_img;
char key_pressed;
int current_filter = 0;

void setup()
{
  surface.setResizable(true);

  original_img = loadImage("test.jpg");
  surface.setSize(original_img.width, original_img.height);

  display_img = createImage(original_img.width, original_img.height, ARGB);
  deepCopy();
}

void deepCopy()
{
  display_img.copy(original_img, 0, 0, original_img.width, original_img.height, 0, 0, display_img.width, display_img.height);
}

void keyPressed()
{
  key_pressed = key;
  deepCopy();
  noTint();
}

void draw()
{
  //default
  if(key_pressed == '0')
  {
    image(display_img, 0, 0);
  }
  //grayscale
  if(key_pressed == '1')
  {
    myGrayscale(original_img,display_img);
    
    image(display_img, 0, 0);
  }
  //contrast
  if(key_pressed == '2')
  {
    myContrast(original_img,display_img);
    
    image(display_img, 0, 0);
  }
  //Gaussian blur
  if(key_pressed == '3')
  {
    myGBlur(original_img,display_img);
    
    image(display_img, 0, 0);
  }
  //edge detection
  if(key_pressed == '4')
  {
    myEDetection(original_img,display_img);
    
    image(display_img, 0, 0);
  }
  
  if(key_pressed == '5')
  {
    mySharpen(original_img,display_img);
    
    image(display_img, 0, 0);
  }
}


void myContrast(PImage source, PImage output)
{
  int brightness_threshold = 127;
  int brightness_change = 80;
  
  colorMode(HSB);
  // traverse pixels
  for (int y = 0; y < source.height; y++) 
  {
    for (int x = 0; x < source.width; x++) 
    {
      // each pixel:
      int loc = x + y*source.width;

      float h = hue(source.pixels[loc]);
      float s = saturation(source.pixels[loc]);
      float b = brightness(source.pixels[loc]);
      
      if (b <= brightness_threshold) //dark
      {
        b -= brightness_change;
      }
      else //bright
      {
        b += brightness_change;
      }

      // send rgb to output
      h = constrain(abs(h), 0, 255);
      s = constrain(abs(s), 0, 255);
      b = constrain(abs(b), 0, 255);
      output.pixels[loc] =  color(h, s, b);
    }
  }
  colorMode(RGB);
  output.updatePixels();
}


void myGrayscale(PImage source, PImage output)
{
  // traverse pixels
  for (int y = 0; y < source.height; y++) 
  {
    for (int x = 0; x < source.width; x++) 
    {
      // each pixel:
      int loc = x + y*source.width;

      float r = red(source.pixels[loc]);
      float g = green(source.pixels[loc]);
      float b = blue(source.pixels[loc]);
      float av = (r+g+b)/3;

      // send rgb to output
      av = constrain(abs(av), 0, 255);
      output.pixels[loc] =  color(av);
    }
  }
  output.updatePixels();
}


void mySharpen(PImage source, PImage output)
{
  float[][] matrix = {{0, -1, 0}, {-1, 5, -1}, {0, -1, 0}};


  // traverse pixels
  for (int y = 1; y < source.height-1; y++) 
  {
    for (int x = 1; x < source.width-1; x++) 
    {
      // each pixel:
      int loc = x + y*source.width;
      float r = 0;
      float g = 0;
      float b = 0;

      // traverse neighbors
      for (int i = 0; i < 3; i++) 
      {
        for (int j = 0; j < 3; j++) 
        {
          // each neighbor pixel(including center)
          int index = (x + i - 1) + source.width*(y + j - 1);
          r += red(source.pixels[index]) * matrix[i][j];
          g += green(source.pixels[index]) * matrix[i][j];
          b += blue(source.pixels[index]) * matrix[i][j];
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


void myGBlur(PImage source, PImage output)
{
  float[][] matrix = {{0.0625, 0.125, 0.0625}, {0.125, 0.25, 0.125}, {0.0625, 0.125, 0.0625}};


  // traverse pixels
  for (int y = 1; y < source.height-1; y++) 
  {
    for (int x = 1; x < source.width-1; x++) 
    {
      // each pixel
      int loc = x + y*source.width;
      float r = 0;
      float g = 0;
      float b = 0;

      // traverse neighbors
      for (int i = 0; i < 3; i++) 
      {
        for (int j = 0; j < 3; j++) 
        {
          // each neighbor pixel(including center)
          int index = (x + i - 1) + source.width*(y + j - 1);
          r += red(source.pixels[index]) * matrix[i][j];
          g += green(source.pixels[index]) * matrix[i][j];
          b += blue(source.pixels[index]) * matrix[i][j];
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


void myEDetection(PImage source, PImage output)
{
  float[][] Xmatrix = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
  float[][] Ymatrix = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};


  // traverse pixels
  for (int y = 1; y < source.height-1; y++) 
  {
    for (int x = 1; x < source.width-1; x++) 
    {
      // each pixel:
      int loc = x + y*source.width;
      float rx = 0;
      float gx = 0;
      float bx = 0;
      float ry = 0;
      float gy = 0;
      float by = 0;
      float rm = 0;
      float gm = 0;
      float bm = 0;

      // traverse neighbors
      for (int i = 0; i < 3; i++) 
      {
        for (int j = 0; j < 3; j++) 
        {
          // each neighbor pixel(including center)
          int index = (x + i - 1) + source.width*(y + j - 1);
          rx += red(source.pixels[index]) * Xmatrix[i][j];
          gx += green(source.pixels[index]) * Xmatrix[i][j];
          bx += blue(source.pixels[index]) * Xmatrix[i][j];
          ry += red(source.pixels[index]) * Ymatrix[i][j];
          gy += green(source.pixels[index]) * Ymatrix[i][j];
          by += blue(source.pixels[index]) * Ymatrix[i][j];
        }
      }
      // end traverse neighbors

      // send rgb to output
      rx = constrain(abs(rx), 0, 255);
      gx = constrain(abs(gx), 0, 255);
      bx = constrain(abs(bx), 0, 255);
      ry = constrain(abs(ry), 0, 255);
      gy = constrain(abs(gy), 0, 255);
      by = constrain(abs(by), 0, 255);
      
      rm = sqrt(pow(rx,2) + pow(ry,2));
      gm = sqrt(pow(gx,2) + pow(gy,2));
      bm = sqrt(pow(bx,2) + pow(by,2));
      
      output.pixels[loc] =  color(rm, gm, bm);
    }
  }
  output.updatePixels();
}
