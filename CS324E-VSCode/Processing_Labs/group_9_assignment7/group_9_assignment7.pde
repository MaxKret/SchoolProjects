//globals
Player player1;
CloudGroup clouds;
Game runningGame;
boolean gameRunning;
boolean firstGame = true;

//setup
void setup()
{
  //init
  size(540,760);
  player1 = new Player();
  clouds = new CloudGroup();
  clouds.seePlayer(player1);
  runningGame = new Game();
  runningGame.seePlayer(player1);
  runningGame.seeClouds(clouds);
  runningGame.startGame();
  
  textSize(50);
  textAlign(CENTER);
  
}


//draw
void draw()
{
  background(0,200,255);

  //displayText(); 
  if (gameRunning) {
    player1.display();
    clouds.displayAll();
    gameRunning = runningGame.tickGame();
    firstGame = false;
  } else{
    if (firstGame){
      background(255,150,0);
      text("Press x to start game", width/2, height/2);
      text("Use WASD to move", width/2, height/2 + 100);
    } else{
      background(255,150,0);
      text("Game Over", width/2, height/4);
      text("Score: " + runningGame.score, width/2, height/2);
      text("Press x to play again", width/2, height/2+150);
      clouds = new CloudGroup();
      player1.resetSprite();
    }
  }
}


//event handling
void keyPressed()
{
  if(key != CODED) player1.keys[key] = true;
  if (key == 'x') {
    gameRunning = true;
    runningGame = new Game();
    runningGame.seePlayer(player1);
    runningGame.seeClouds(clouds);
    runningGame.startGame();
  }
}

void keyReleased()
{
  if(key != CODED) player1.keys[key] = false;
}
