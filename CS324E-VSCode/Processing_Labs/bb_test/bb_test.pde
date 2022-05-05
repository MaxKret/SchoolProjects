//globals
int sys_fcount;
int curr_framerate;

int numSpriteFrames = 3;
PImage[] sprite1 = new PImage[numSpriteFrames];
float sprite1_x,sprite1_y,sprite1_scale;

int curr_spriteFrame = 0;

PShape pshp,bb,img;


//setup
void setup()
{
  //init
  size(500,500);
  
  sprite1_scale = 100;
  
  //load frames
  for(int i=0;i<numSpriteFrames;i++)
  {
    String iName = "left"+nf(i+1,1)+".png";
    sprite1[i] = loadImage("sprites/"+iName);
  }
  
  // center sprite location
  //sprite1_x = (width/2) - (sprite1[0].width/2);
  //sprite1_y = (height/2) - (sprite1[0].height/2);
  centerSprite();
  
  
  pshp = createShape(GROUP);
  
  bb = createShape(RECT,15,0,70,100);
  pshp.addChild(bb);
  
  img = createShape(RECT,0,0,100,100);
  pshp.addChild(img);
  
}


//draw
void draw()
{
  background(230);
  
  
  sys_fcount = frameCount;
  curr_spriteFrame = sys_fcount%numSpriteFrames;
  //image(sprite1[curr_spriteFrame],sprite1_x - 100,sprite1_y,sprite1_scale,sprite1_scale);
  img.setTexture(sprite1[curr_spriteFrame]);
  shape(pshp,sprite1_x - 100,sprite1_y);
}

//event handling
void keyPressed()
{
  
  if (key == CODED)
  {
    if (keyCode == UP)
    {
      // frameRate up
      curr_framerate += 1;
      curr_framerate = constrain(curr_framerate,1,120);
    }
    else if (keyCode == DOWN)
    {
      // frameRate down
      curr_framerate -= 1;
      curr_framerate = constrain(curr_framerate,1,120);
    }
    
  }  
  else //key NOT Coded
  {
    if(key == 'w' || key == 'W')
    {// move up
      sprite1_y -= 10;
    }
    if(key == 's' || key == 'S')
    {// move down
      sprite1_y += 10;
    }
    if(key == 'a' || key == 'A')
    {// move left
      sprite1_x -= 10;
    }
    if(key == 'd' || key == 'D')
    {// move right
      sprite1_x += 10;
    }
  }
}


//main methods
void centerSprite()
{
  sprite1_x = (width/2) - ((sprite1_scale)/2);
  sprite1_y = (height/2) - ((sprite1_scale)/2);
}

void resetScene()
{
  centerSprite();
}
