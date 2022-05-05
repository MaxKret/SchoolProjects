//Bezier curve code generator
//Natalie Freed Oct. 2014

DraggableHandler points;

void setup()
{
  size(600, 600);
  points = new DraggableHandler(this);
  points.addToEnd(new DraggableCircle(30, height/2, 10, color(0, 100, 0, 150)));
  points.addToEnd(new DraggableCircle(170, height/4, 10, color(160, 0, 160, 150)));
  points.addToEnd(new DraggableCircle(width-120, height/6, 10, color(255, 0, 255, 150)));
  points.addToEnd(new DraggableCircle(width-30, height/2, 10, color(0, 150, 0, 150)));
}

void draw()
{
  background(100);
  points.display();
  
  noFill();
  stroke(0);
  bezier(points.get(0).getX(), points.get(0).getY(), points.get(1).getX(), points.get(1).getY(), points.get(2).getX(), points.get(2).getY(), points.get(3).getX(), points.get(3).getY());
  fill(0);
  textSize(22);
  text("bezier(" + round(points.get(0).getX()) + ", " + round(points.get(0).getY()) + ", " + round(points.get(1).getX()) + ", " + round(points.get(1).getY()) + ", " + round(points.get(2).getX()) + ", " + round(points.get(2).getY()) + ", " + round(points.get(3).getX()) + ", " + round(points.get(3).getY()) + ");", 20, height*0.75);
  
  fill(255);
  textSize(16);
  text("Click and drag the endpoints and control points to change the bezier curve.", 20, height*0.75+50);
  text("You can copy the generated code from the Processing console.", 20, height*0.75+70);
}

class DraggableCircle implements Draggable
{
  PVector center;
  int radius;
  boolean dragged;
  int fillColor;
  PVector clickOffset; //offset of cursor from center

  DraggableCircle(int centerX, int centerY, int tempRadius, int tempColor)
  {
    center = new PVector(centerX, centerY);
    radius = tempRadius;
    fillColor = tempColor;
    dragged = false;
    PVector clickOffset = new PVector(0, 0);
  }
  
  void display()
  {
    noStroke();
    fill(fillColor);
    ellipse(center.x, center.y, radius*2, radius*2);
  }
  
  float getX()
  {
    return center.x;
  }
  
  float getY()
  {
    return center.y;
  }
  
  boolean isOver(int x, int y)
  {
    //return true if distance between point and center is smaller than radius
    if (dist(center.x, center.y, x, y) <= radius)
    {
      return true;
    }
    else
    {
      return false;
    }
  }
  
  void update() //move with mouse
  {
    if (dragged)
    {
      if(mouseX > 0 && mouseX < width && mouseY > 0 && mouseY < height) //don't let it get away!
      {
        center.set(PVector.add(new PVector(mouseX, mouseY), clickOffset));
      }
    }
  }
  
  void setDragged(int fromX, int fromY)
  {
    dragged = true;
    clickOffset = PVector.sub(center, new PVector(fromX, fromY));
  }
  
  void releaseDragged()
  {
    dragged = false;
  }
}




//You don't need to change anything below here!
//Here in case you want to peek under the hood, but
//there's some slightly weird stuff.
interface Draggable
{
  void update();
  void display();
  void setDragged(int fromX, int fromY);
  void releaseDragged();
  float getX();
  float getY();
  boolean isOver(int x, int y);
}

public class DraggableHandler
{
  ArrayList<Draggable> draggables;
  Draggable currentDragged;

  DraggableHandler(PApplet app)
  {
    draggables = new ArrayList<Draggable>();
    currentDragged = null;
    app.registerMethod("draw", this);
    app.registerMethod("mouseEvent", this);
  }

  void addToEnd(Draggable d)
  {
    draggables.add(d);
  }

  void addToFront(Draggable d)
  {
    draggables.add(0, d); //add to index 0, shift all others
  }

  void remove(Draggable d)
  {
    draggables.remove(d);
  }
  
  Draggable get(int index)
  {
    return draggables.get(index);
  }

  void display()
  {
    for (int i=draggables.size()-1;i>=0;i--) //draw backwards so first will be on top
    {
      draggables.get(i).display();
    }
  }

  public void draw() //this draw is automatically called at the end of each draw()
  {
    for (int i=0;i<draggables.size();i++)
    {
      draggables.get(i).update();
    }
  }

  public void mouseEvent(MouseEvent event)
  {
    int x = event.getX();
    int y = event.getY();

    switch (event.getAction()) {
    case MouseEvent.PRESS:
      // choose top draggable to drag if clicked on
      if (currentDragged == null)
      {
        for (int i=0;i<draggables.size();i++)
        {
          if (draggables.get(i).isOver(x, y))
          {
            currentDragged = draggables.get(i);
            currentDragged.setDragged(x, y);
            break;
          }
        }
      }
      break;
    case MouseEvent.RELEASE:
      // release any dragged objects
      if (currentDragged != null)
      {
        currentDragged.releaseDragged();
        currentDragged = null;
      }
      break;
    case MouseEvent.CLICK:
      // 
      break;
    case MouseEvent.DRAG:
      // 
      break;
    case MouseEvent.MOVE:
      // 
      break;
    }
  }
}

void mouseDragged()
{
  println("bezier(" + round(points.get(0).getX()) + ", " + round(points.get(0).getY()) + ", " + round(points.get(1).getX()) + ", " + round(points.get(1).getY()) + ", " + round(points.get(2).getX()) + ", " + round(points.get(2).getY()) + ", " + round(points.get(3).getX()) + ", " + round(points.get(3).getY()) + ");");
}
