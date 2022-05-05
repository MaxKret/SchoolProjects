class celestialObject {
  PShape center;
  PShape[] rays;
  float x_loc;
  float y_loc;
  int[] direction = {-1 , -1};
  color object_color;

  public celestialObject(boolean is_sun) {
    if (is_sun) {
      object_color = #DBF539;
    } else {
      object_color = #868AA7;
    }
    center = createShape(ELLIPSE, x_loc, y_loc, 75.0, 75.0);

  }

  public void move() {
    x_loc += direction[0] * 10;
    y_loc += direction[0] * 10;
  }


  public void display() {
    fill(object_color);
    shape(center);
  }

  public void wrap(int x, int y) {
    x_loc = x;
    y_loc = y;
  }

  public void changeDir() {
    direction[1] = -direction[1];
  }
}


class sky {
  int timeH;
  int timeM;
  celestialObject[] bodies;
  static color DAY_COLOR = #5A92EA;
  static color NIGHT_COLOR = #000000;
  boolean is_day;
  int[] worldSize;

  sky(celestialObject[] bodies, int[] worldSize) {
    timeH = 0;
    timeM = 0;
    is_day = true;
    this.bodies = bodies; //Sun is body 0
    this.worldSize = worldSize;
  }



  public void tickTime() {
    timeM += 1;
    if (timeM == 60) {
      timeH += 1;
      timeM = 0;
      if (timeH == 13) {
        timeH = 0;
        for (int i = 0; i <= bodies.length; i++) {
          bodies[i].changeDir();
        }
      } else if (timeH == 6) {
        is_day = !is_day;
        if (is_day) {
          bodies[0].wrap(worldSize[0], worldSize[1]);
        } else {
          bodies[1].wrap(worldSize[0], worldSize[1]);
        }
      }
    }
  }
  public color getColor() {
    if (is_day) {
      return DAY_COLOR;
    } else {
      return NIGHT_COLOR;
    }
  }

  public void progress() {
    tickTime();
    for (int i = 0; i <= bodies.length; i++) {
      bodies[i].move();
      bodies[i].display();
    }
  }
}
