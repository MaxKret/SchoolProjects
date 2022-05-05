float x1,x2,x3,x4 = 0.0;
float x5 = 400.0;
float easing = 0.05;
float easingIn = 0.001;
float sinAngle = 0.0;
void setup () 
{
  size(800, 500);
  
}

void draw() 
{
  //background(255);
  int targetX = 700;
  
  // OG ease-out
  fill(255,0,0);
  x1 += (targetX - x1) * easing;
  ellipse(x1, 50, 50, 50);
  
  // OG ease-in
  fill(255,255,0);
  if(x2<targetX)
  {
    x2 += (1 + x2) * easing;
  }
  ellipse(x2, 100, 50, 50);
  
  // lerp ease-out
  fill(0,255,0);
  x3 = lerp(x3, targetX, easing);
  ellipse(x3, 150, 50, 50);
  
  // lerp ease-in
  fill(0,255,255);
  x4 = lerp(x4, targetX, easingIn);
  ellipse(x4, 200, 50, 50);
  easingIn *= 1.1;
  
  float dx1 = 40*sin(sinAngle);
  sinAngle += 0.1;
  fill(0,0,255);
  ellipse(x5+dx1, 250, 50, 50);
  
  float dx2 = 40*sin(sinAngle);
  float dy2 = 40*cos(sinAngle);
  //sinAngle += 0.1;
  fill(255,0,255);
  ellipse(x5+dx2, 350+dy2, 50, 50);
  
  
  /*x += (.1 + x) * easing;
  y += -3;
  ellipse(x, y, 50, 50);*/
}
