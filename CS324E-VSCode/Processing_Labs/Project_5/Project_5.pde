Cube cb;

void setup() {
  frameRate(60);
  size(640, 360, P3D);
  background(0);
  cb = new Cube(300, 600, 100);

}

void draw() {
  background(255);
  directionalLight(0,255,0,0,-1,0);
  directionalLight(255,0,0,0,1,0);
  //translate(200, 100, 0); 
  cb.drawPyramid();
  //py.rotatePyramid();
  //translate(100, 100, 0); 
  //shape(py);
  //py.rotateY(2);
  
  //camera(mouseX, mouseY, 200.0,
  //  0.0, 0.0, 0.0,
  //  0.0, 200, 0.0);
}
