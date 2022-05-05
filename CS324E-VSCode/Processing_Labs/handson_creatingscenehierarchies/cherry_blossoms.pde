class cherry_blossoms{
  //default constructor
  cherry_blossoms(){}
  
  //create multipul blossoms
  //Parameters are starting x value, starting y value, and starting angle
  cherry_blossom a = new cherry_blossom(0,0,0.2); 
  cherry_blossom b = new cherry_blossom(-50,30,0); 
  cherry_blossom c = new cherry_blossom(-50,-22,1);
  cherry_blossom d = new cherry_blossom(-45,-0,0.7); 
  cherry_blossom e = new cherry_blossom(-31,-10,1.4); 
  cherry_blossom f = new cherry_blossom(-70,0,0); 
  cherry_blossom g = new cherry_blossom(30,-60,1); 
  cherry_blossom h = new cherry_blossom(66,-66,2.5); 
  cherry_blossom i = new cherry_blossom(-30,-22,1.5); 
  cherry_blossom j = new cherry_blossom(-20,-22,1.3); 
  cherry_blossom k = new cherry_blossom(-50,-77,1.1); 
  cherry_blossom l = new cherry_blossom(20,-44,0.9); 
  cherry_blossom m = new cherry_blossom(-55,-15,0.7); 
  cherry_blossom n = new cherry_blossom(-34,-34,0.5); 
  
  void allFall(){
    //parameters are amount of rotation each frame, fall speed in x direction, and fall speed in y direction
    //For best results, keep amount of rotation between 0.005 - 0.035
    //Keep fall speed in x or y direction between 0.5 - 3.5
    a.fall(0.02, 1, 2);
    b.fall(0.01, 1.5, 1);
    c.fall(0.03, 2, 1.3);
    d.fall(0.013, 1.2, 0.7);
    e.fall(0.013, 1.1, 1.1);
    f.fall(0.004, 0.8, 2);
    g.fall(0.015, 0.5, 1.3);
    h.fall(0.02, 1.2, 1.2);
    i.fall(0.024, 1.6, 1);
    j.fall(0.009, 0.7, 0.7);
    k.fall(0.02, 1.5, 0.6);
    l.fall(0.015, 2, 0.5);
    m.fall(0.022, 0.5, 0.5);
    n.fall(0.011, 2.2, 0.4);
  }
}
