//globals
int sys_fcount;
int curr_framerate;

int numSpriteFrames = 16;
PImage[] sprite1 = new PImage[numSpriteFrames];
float sprite1_x,sprite1_y,sprite1_scale;

int curr_spriteFrame = 0;

int animationTimer = 0;
int animationTimerValue = 50;
int curr_spriteFrameMillis = 0;

Timer timer1;
int curr_spriteFrameTimers = 0;

ButtonRect playBtn,pauseBtn;


//setup
void setup()
{
  //init
  size(500,500);
  frameRate(24);
  curr_framerate = 24;
  sprite1_scale = 100;
  
  //button setup
  playBtn = new ButtonRect((width/2-16)-25, height-40, 30, 30, color(110), color(255));
  pauseBtn = new ButtonRect((width/2-16)+25, height-40, 30, 30, color(110), color(255));
  
  //load frames
  for(int i=0;i<numSpriteFrames;i++)
  {
    String iName = "run"+nf(i+1,2)+".png";
    sprite1[i] = loadImage("run_animation/"+iName);
  }
  
  //timer class
  timer1  = new Timer();
  
  // center sprite location
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
  curr_spriteFrame = sys_fcount%numSpriteFrames;
  image(sprite1[curr_spriteFrame],sprite1_x - 100,sprite1_y,sprite1_scale,sprite1_scale);
  
  
  image(sprite1[curr_spriteFrameMillis], sprite1_x,sprite1_y,sprite1_scale,sprite1_scale);
  if ((millis() - animationTimer) >= animationTimerValue) 
  {
    curr_spriteFrameMillis = (curr_spriteFrameMillis + 1) % numSpriteFrames;
    animationTimer = millis();
  }
  
  image(sprite1[curr_spriteFrameTimers],sprite1_x + 100,sprite1_y,sprite1_scale,sprite1_scale);
  if(timer1.trigger_action)
  {
    curr_spriteFrameTimers = (curr_spriteFrameTimers+1) % numSpriteFrames;
  }
  timer1.update();
  
  displayText();
  
  playBtn.update();
  playBtn.display();
  pauseBtn.update();
  pauseBtn.display();
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
  if(playBtn.isPressed()) timer1.play();
  else if(pauseBtn.isPressed()) timer1.pause();
  else resetScene();
}

void mouseReleased()
{
  playBtn.isReleased();
  pauseBtn.isReleased();
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
  curr_framerate = 24;
}

void displayText()
{
  // info
  fill(0);
  text("WASD for movement, UP/DOWN arrows for framecount change, click to reset",0,10);
  text("Current Sprite Pos: ("+sprite1_x+","+sprite1_y+")",0,25);
  text("Current Sys Frame, Current Millis(): "+frameCount+", "+millis(),0,40);
  text("Current Sys frameRate: "+frameRate,0,55);
  text("Current set frameRate: "+curr_framerate,0,70);
  text("Current Sprite Frame: "+curr_spriteFrame,0,90);
  text("Current Millis Sprite Frame: "+curr_spriteFrameMillis,0,105);
  text("Current Timers Sprite Frame: "+curr_spriteFrameTimers,0,120);
  // labels for sprites
  text("Using frameCount",sprite1_x-100-20,sprite1_y);
  text("Using Millis",sprite1_x,sprite1_y);
  text("Using Timer Class",sprite1_x+100,sprite1_y);
  // button labels
  text("Play",playBtn.x+4,playBtn.y);
  text("Pause",pauseBtn.x-1,pauseBtn.y);
  
  fill(255);
}
