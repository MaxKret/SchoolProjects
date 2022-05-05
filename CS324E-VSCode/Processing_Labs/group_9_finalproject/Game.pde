class Game {
  int score;
  int startTime;
  boolean playerAlive;
  
  Player thisPlayer;
  CloudGroup thisClouds;
  
  Game() {
    score = 0;
    playerAlive = true;
    
  }

  void startGame() {
    startTime = millis();
  }

  boolean tickGame() {
    playerAlive = !thisClouds.checkCollisions();
    if (playerAlive) {
      score = millis() - startTime;
      text(str(score), width/2, height/14);
    } else {
      return false;
    }
    //Move Clouds here
    return true;
  }
  
  void seePlayer(Player newPlayer){
    thisPlayer = newPlayer;
  }
  
  void seeClouds(CloudGroup newClouds){
    thisClouds = newClouds;
  }
}
