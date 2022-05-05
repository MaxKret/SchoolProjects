class CloudParticles {
  int frame = 0;
  
  //default constructor
  CloudParticles(){
    
  }
  
  void displayParticles(int cloudXPos, int cloudYPos){
    stroke(0);
    fill(255);
    PShape a = createShape(RECT, cloudXPos+10, cloudYPos-(frame*random(0,4)), 4, 4);
    PShape b = createShape(RECT, cloudXPos+24, cloudYPos-(frame*random(0,4)), 4, 4);
    PShape c = createShape(RECT, cloudXPos+37, cloudYPos-(frame*random(0,4)), 4, 4);
    PShape d = createShape(RECT, cloudXPos+56, cloudYPos-(frame*random(0,4)), 4, 4);
    PShape e = createShape(RECT, cloudXPos+69, cloudYPos-(frame*random(0,4)), 4, 4);
    
    if (frame >= 15){
      frame = 0;
    } else{
      frame += 1;
    }
    
    shape(a);
    shape(b);
    shape(c);
    shape(d);
    shape(e);
  }
}
