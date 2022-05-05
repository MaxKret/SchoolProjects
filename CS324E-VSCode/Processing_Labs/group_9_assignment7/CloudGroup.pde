Player player;

class CloudGroup{
  Cloud a, b, c, d, e;
  CloudGroup(){
    this.a = new Cloud(50,-50,2);
    this.b = new Cloud(150,-100,3);
    this.c = new Cloud(250,0,6);
    this.d = new Cloud(300,-150,4);
    this.e = new Cloud(450,-200,5);
  }
  
  void displayAll(){
    a.display();
    b.display();
    c.display();
    d.display();
    e.display();
    
    a.descend();
    b.descend();
    c.descend();
    d.descend();
    e.descend();
    

  }
  
  void seePlayer(Player newPlayer){
    player = newPlayer;
  }
  
  boolean checkCollision(Cloud cloud){
    if(cloud.cloud.contains(player.posx, player.posy) || //<>//
      cloud.cloud.contains(player.posx+player.bwidth, player.posy) ||
      cloud.cloud.contains(player.posx, player.posy+player.bheight) || 
      cloud.cloud.contains(player.posx+player.bwidth, player.posy+player.bheight)){
        print("Game Over");
        return true;
      }
     return false;
  }
  
  boolean checkCollisions(){
    return checkCollision(a) ||
    checkCollision(b) ||
    checkCollision(c) ||
    checkCollision(d) ||
    checkCollision(e);
  }
}
