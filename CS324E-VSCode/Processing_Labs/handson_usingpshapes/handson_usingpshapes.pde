void setup()
{
  size(500,500);
  background(200);
}

void draw()
{
  // free hand
  beginShape();//folded napkin
  vertex(30, 20);
  vertex(85, 20);
  vertex(85, 75);
  vertex(30, 75);
  vertex(30, 20);
  vertex(85, 75);
  vertex(85, 20);
  vertex(30, 75);
  endShape();
  
  //triangle strip
  beginShape(TRIANGLE_STRIP);// folded  napkin hat
  vertex(130, 20);
  vertex(130, 75);
  vertex(185, 75);
  vertex(185, 20);
  endShape();
  
  PShape folded_napkin = createShape();
  folded_napkin.beginShape();//folded napkin
  folded_napkin.vertex(30, 20);
  folded_napkin.vertex(85, 20);
  folded_napkin.vertex(85, 75);
  folded_napkin.vertex(30, 75);
  folded_napkin.vertex(30, 20);
  folded_napkin.vertex(85, 75);
  folded_napkin.vertex(85, 20);
  folded_napkin.vertex(30, 75);
  folded_napkin.endShape();
  //pshape group
  PShape person = createShape(GROUP);
  PShape head = createShape(ELLIPSE, 159, 105, 50, 50);
  PShape body = createShape(RECT, 134, 130, 50, 100);
  fill(0);
  PShape left_eye = createShape(ELLIPSE, 150, 105, 10, 10);
  PShape right_eye = createShape(ELLIPSE, 168, 105, 10, 10);
  fill(255);
  person.addChild(head);
  person.addChild(body);
  person.addChild(left_eye);
  person.addChild(right_eye);
  shape(person);
  
  
  //bezier curve
  PVector v1 = new PVector(160+100, 150);
  PVector v2 = new PVector(160+100, 200);
  PVector c1 = new PVector(195+100,  96);
  PVector c2 = new PVector(244+100, 159);
  PVector c3 = new PVector(125+100,  96);
  PVector c4 = new PVector(76+100,  159);
  beginShape();// right heart
  vertex(v1.x,v1.y);
  bezierVertex(c1.x,c1.y,c2.x,c2.y,v2.x,v2.y);
  endShape();
  
  beginShape();// left heart
  vertex(v1.x,v1.y);
  bezierVertex(c3.x,c3.y,c4.x,c4.y,v2.x,v2.y);
  endShape();
}
