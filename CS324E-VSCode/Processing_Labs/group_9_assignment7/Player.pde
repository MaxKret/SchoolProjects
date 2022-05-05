class Player
{
  //fields
  int numSpriteFrames = 3;
  PImage[] leftSprite = new PImage[numSpriteFrames];
  PImage[] rightSprite = new PImage[numSpriteFrames];
  float posx,posy,scale,speed,bwidth,bheight;
  PShape bound_box,sprite_group,sprite_img;
  
  int curr_spriteFrame = 0;
  int sys_fcount;
  
  boolean[] keys = new boolean[128];
  boolean left_mode = true;
  
  
  //constructor
  Player()
  {
    scale = 100;
    speed = 6;
  
    //load frames
    for(int i=0;i<numSpriteFrames;i++)
    {
      String iName = "left"+nf(i+1,1)+".png";
      leftSprite[i] = loadImage("sprites/"+iName);
    } 
    for(int i=0;i<numSpriteFrames;i++)
    {
      String iName = "right"+nf(i+1,1)+".png";
      rightSprite[i] = loadImage("sprites/"+iName);
    }
    
    resetSprite();
    
    sprite_group = createShape(GROUP);
    
    bwidth = 70;
    bheight = 100;
    bound_box = createShape(RECT,15,0,bwidth,bheight);
    bound_box.beginShape();
    bound_box.noFill();
    bound_box.endShape();
    sprite_group.addChild(bound_box);
    
    sprite_img = createShape(RECT,0,0,scale,scale);
    sprite_group.addChild(sprite_img);
    
  }
  
  
  
  //class methods
  void display()
  {
    sys_fcount = frameCount;
    curr_spriteFrame = sys_fcount%numSpriteFrames;
    
    move();
    
    if(left_mode) sprite_img.setTexture(leftSprite[curr_spriteFrame]);
    else sprite_img.setTexture(rightSprite[curr_spriteFrame]);
    shape(sprite_group,posx,posy);
  }
  
  void move()
  {  
    if(keys['w'] || keys['W'])
    {// move up
      if((posy)-speed > 0)
      {
        posy -= speed;
      }
    }
    if(keys['s'] || keys['S'])
    {// move down
      if((posy+bheight)+speed < height)
      {
        posy += speed;
      }
    }
    if(keys['a'] || keys['A'])
    {// move left
      if((posx+15)-speed > 0)
      {
        posx  -= speed;
      }
      left_mode = true;
    }
    if(keys['d'] || keys['D'])
    {// move right
      if(((posx+15)+bwidth)+speed < width)
      {
        posx += speed;
      }
      left_mode = false;
      
    }
  }
  
  void resetSprite()
  {
    posx = (width/2) - ((scale)/2);
    posy = (height-100) - ((scale)/2);
  }
  
}
