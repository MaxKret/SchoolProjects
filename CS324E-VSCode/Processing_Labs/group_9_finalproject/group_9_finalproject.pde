import processing.sound.*; //<>//
SoundFile sway;
SoundFile gameOver;

//globals
Player player1;
CloudGroup clouds;
Game runningGame;
boolean gameRunning;
boolean firstGame = true;
boolean muted = false;
PFont ourfont;

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
  
  ourfont = createFont("Minecraft.ttf", 50);
  textFont(ourfont);
  textSize(50);
  textAlign(CENTER);
  
  //sound stuff
  sway = new SoundFile(this, "swayv3.mp3");
  gameOver = new SoundFile(this, "Gameover.mp3");
  if (muted == false){
      gameOver.stop();
      sway.loop(1, 0.25);
    } else{
      sway.stop();
      gameOver.stop();
    }
}


//draw
void draw()
{
  background(0,200,255);

  if (gameRunning) 
  {
    player1.display();
    clouds.displayAll();
    gameRunning = runningGame.tickGame();
    firstGame = false;
    player1.scoreChecked = false;
    
    //playGameMusic();
  } 
  else // game not running
  {
    if (firstGame)
    {
      background(255,150,0);
      text("Press x to start game", width/2, height/2);
      text("Use WASD to move", width/2, height/2 + 100);
    } 
    else
    {
      background(255,150,0);
      boolean new_highscore;
      new_highscore = player1.checkHighscore(runningGame.score);
      player1.scoreChecked = true;
      if(new_highscore)
      {
        text("New High Score!!!", width/2, height/2+75);
      }
      text("Game Over", width/2, height/4);
      text("Score: " + runningGame.score, width/2, height/2);
      text("Press x to play again", width/2, height/2+150);
      clouds = new CloudGroup();
      player1.resetSprite();
      
      //if (muted == false){
      //  sway.stop();
      //  gameOver.play(1, 0.25);
      //} else{
      //  sway.stop();
      //  gameOver.stop();
      //}
    }
  }
}


//void playGameOverMusic()
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

void mousePressed(){
  if (muted == true){
      sway.loop(1);
      muted = false;
    } else{
      sway.stop();
      muted = true;
    }
}

void keyReleased()
{
  if(key != CODED) player1.keys[key] = false;
}
