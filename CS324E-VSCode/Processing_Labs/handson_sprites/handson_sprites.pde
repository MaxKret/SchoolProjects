//globals
int nFrames = 16;
PImage[] sprite1 = new PImage[nFrames];
float sprite1_x,sprite1_y,sprite1_scale;
int curr_spriteFrame;

int sys_fcount;
int curr_framerate;


//setup
void setup()
{
  //init
  size(500,500);
  frameRate(24);
  curr_framerate = 24;
  sprite1_scale = 100;
  
  //load frames
  for(int i=0;i<nFrames;i++)
  {
    String iName = "run"+nf(i+1,2)+".png";
    sprite1[i] = loadImage("run_animation/"+iName);
  }
  
  // center sprite location; does this but uses scale=100 instead of wd and ht
  //sprite1_x = (width/2) - (sprite1[0].width/2);
  //sprite1_y = (height/2) - (sprite1[0].height/2);
  centerSprite();
}


//draw
void draw()
{
  frameRate(curr_framerate);
  background(230);
  
  sys_fcount = frameCount;
  curr_spriteFrame = sys_fcount%nFrames;
  image(sprite1[curr_spriteFrame],sprite1_x,sprite1_y,sprite1_scale,sprite1_scale);
  
  displayText();
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

void mousePressed()
{
  centerSprite();
  curr_framerate = 24;
}


//main methods
void centerSprite()
{
  sprite1_x = (width/2) - ((sprite1_scale)/2);
  sprite1_y = (height/2) - ((sprite1_scale)/2);
}

void displayText()
{
  fill(0);
  text("WASD for movement, UP/DOWN arrows for framecount change, click to reset",0,10); //<>//
  text("Current Sys Frame: "+frameCount,0,25);
  text("Current Sprite Frame: "+curr_spriteFrame,0,40);
  text("Current Sys frameRate: "+frameRate,0,55);
  text("Current set frameRate: "+curr_framerate,0,70);
  text("Current Sprite Pos: ("+sprite1_x+","+sprite1_y+")",0,85);
  fill(255);
}
