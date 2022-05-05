//globals
import processing.sound.*;
SoundFile file;
sky sky;
celestialObject[] bodies;
Tree roseBlossomTree;
cherry_blossoms blossoms;

//setup
void setup()
{
  file = new SoundFile(this, "lullaby.mp3");
  file.loop(1, 0.25);
  size(960,540); // res:1920x1080; half:960x540; 3/4: 1440x810
  int[] Size = {960, 540};
  celestialObject c1 = new celestialObject(true);
  celestialObject c2 = new celestialObject(false);
  bodies = new celestialObject[2];
  bodies[0] = c1;
  bodies[1] = c2;
  sky = new sky(bodies, Size);
  roseBlossomTree = new Tree(); 
  blossoms = new cherry_blossoms();
}

//draw loop
void draw()
{
  background(sky.getColor());
  sky.progress();
  roseBlossomTree.move();
  blossoms.allFall();
  
}
