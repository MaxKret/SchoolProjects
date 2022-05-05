class PlayerSmoke
{
  //fields
  boolean flipped;
  
  
  //constructor
  PlayerSmoke()
  {
    
    
  }
  
  void display(float x, float y)
  {
    float y_offset = 5;
    noFill();
    stroke(#818181);
    if(flipped)
    {
      arc(x, y+y_offset/2, 4,5, HALF_PI,HALF_PI*3); // top on bottom
      arc(x, y-y_offset/2, 4,5, -HALF_PI,HALF_PI); // bottom on top
    }
    else
    {
      arc(x, y-y_offset/2, 4,5, HALF_PI,HALF_PI*3); // top on top
      arc(x, y+y_offset/2, 4,5, -HALF_PI,HALF_PI); // bottom on bottom
    }
    stroke(0);
    
    float sys_fcount = frameCount;
    if(sys_fcount%4 == 0)
    { flipped = !flipped; }
   
  }
}
