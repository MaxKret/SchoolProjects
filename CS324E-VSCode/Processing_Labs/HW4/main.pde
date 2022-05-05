sky sky;
celestialObject[] bodies;

public void setup(){
  size(960,540);
  int[] Size = {960, 540};
  bodies[0] = new celestialObject(true);
  bodies[1] = new celestialObject(false);
sky = new sky(bodies, Size);
}

public void draw(){
sky.progress();

}
