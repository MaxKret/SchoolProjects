float t1, t2, tvalue = 0.0;
float i, j = 0.0;
float stepSize = 100.0;
float xOut, xOutCos = 0.0;

void setup () 
{
  size(600, 600);
}

void draw() 
{
  
  background(210);
   
  int x1 = 60;
  int x2 = 540;
  
  // lerp method
  if (i <= 100.0)
  {
    t1 = i/100.0;
    float x = lerp(x1, x2, t1);
    fill(255,0,0);
    ellipse(x, 15, 30, 30);
    i++;
  }
  
  // general lin interp equation
  if (j <= 100.0)
  {
    t2 = j/100.0;
    float lerpX = (x1*(1-t2)) + (x2*t2);
    fill(0,255,0);
    ellipse(lerpX, 55, 30, 30);
    j++;
  }
  
  // move methods
  stepSize = 100.0;
  
  xOut = moveLerp(x1,x2,tvalue,stepSize);
  fill(0,0,255);
  ellipse(xOut, 95, 30, 30);
  
  xOutCos = moveCosLerp(x1,x2,tvalue,stepSize);
  fill(255,0,255);
  ellipse(xOutCos, 135, 30, 30);
  
  tvalue++;
}

float moveLerp(float v0, float v1, float t3, float step)
{
  float returnX = 0.0;
  if (t3 <= step)
  {
    returnX = lerp(v0,v1,t3/step); // (v0*(1-t3)) + (v1*t3)
  }
  else
  {
    returnX = v1;
  }
  return returnX;
}

float moveCosLerp(float v0, float v1, float t3, float step)
{
  float returnX = 0.0;
  if (t3 <= step)
  {
    float tCos = (1-cos(PI*(t3/step)))/2;
    returnX = lerp(v0,v1,tCos); // (v0*(1-t3)) + (v1*t3)
  }
  else
  {
    returnX = v1;
  }
  return returnX;
}
