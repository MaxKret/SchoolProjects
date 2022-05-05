class celestialObject {
  PShape center;
  float x_loc;
  float y_loc;
  int[] direction = {-1, -1};
  color object_color;
  boolean isSun;
  float r;

  public celestialObject(boolean isSun) {
    this.isSun = isSun;
    if (isSun) {
      object_color = #bc002d;
    } else {
      object_color = #FFE790;
    }
    x_loc = -1000;
    y_loc = -1000;
    center = createShape(ELLIPSE, x_loc, y_loc, 75.0, 75.0);
  }

  public void move() {
    x_loc += direction[0] * 2;
    y_loc += direction[1];
    r += -direction[1] * .5;
  }


  public void display() {
    fill(object_color);
    center = createShape(ELLIPSE, x_loc, y_loc, r, r);
    shape(center);
  }

  public void wrap(int x) {
    x_loc = x;
    y_loc = 200;
    r = 75;
  }

  public void changeDir(int timeH, boolean isDay) {
    if (timeH == 10) {
      direction[0] = -1;
      direction[1] = 0;
    } else if ((timeH ==  6) && ((!isSun && isDay) || (isSun && !isDay))){
      direction[0] = -1;
      direction[1] = -1;
    } else if(timeH == 5){
      direction[0] = -1;
      direction[1] = 1;

    }
  }
}


class sky {
  int timeH;
  int timeM;
  celestialObject[] bodies;
  boolean is_day;
  int[] worldSize;
  color[] dayColors = new color[12];
  color[] nightColors = new color[12];
  color c6 = color(90,146,234); // true blue
  color c5 = color(75,110,187);
  color c4 = color(60,80,140);
  color c3 = color(45,60,93);
  color c2 = color(30,30,46);
  color c1 = color(0); // true black
  

  sky(celestialObject[] bodies, int[] worldSize) {
    timeH = 0;
    timeM = 0;
    is_day = false;
    this.bodies = bodies; //Sun is body 0
    this.worldSize = worldSize;
    
    dayColors[0] = c6;
    dayColors[1] = c5;
    dayColors[2] = c4;
    dayColors[3] = c3;
    dayColors[4] = c3;
    dayColors[5] = c3; 
    dayColors[6] = c3;
    dayColors[7] = c5;
    dayColors[8] = c6;
    dayColors[9] = c6;
    dayColors[10] = c6;
    dayColors[11] = c6;
    
    nightColors[0] = c1;
    nightColors[1] = c1;
    nightColors[2] = c1;
    nightColors[3] = c2;
    nightColors[4] = c3;
    nightColors[5] = c3; 
    nightColors[6] = c3;
    nightColors[7] = c3;
    nightColors[8] = c2;
    nightColors[9] = c1;
    nightColors[10] = c1;
    nightColors[11] = c1;
  }



  public void tickTime() {
    timeM += 2;
    if (timeM == 60) {
      timeH += 1;
      timeM = 0;
      for (int i = 0; i < bodies.length; i++) {
        bodies[i].changeDir(timeH, is_day);
      }
      if (timeH == 12) 
      {
        timeH = 0;
      } 
      else if (timeH == 6) 
      {
        is_day = !is_day;
        if (is_day) 
        {
          bodies[0].wrap(worldSize[0]);
        } 
        else 
        {
          bodies[1].wrap(worldSize[0]);
        }
      }
    }
  }
  
  public color getColor() 
  {
    if (is_day) {
      return dayColors[timeH];
    } else {
      return nightColors[timeH];
    }
  }

  public void progress() {
    tickTime();
    for (int i = 0; i < bodies.length; i++) {
      bodies[i].move();
      bodies[i].display();
    }
  }
}
