class Timer
{
  // fields
  int msStartTime;
  int interval;

  boolean playing;
  boolean trigger_action;

  //constructor
  Timer()
  {
    playing = true;
    trigger_action = true;
    
    interval = 50;
    msStartTime = 0;
  }

  //methods
  void update()
  {
    if (playing)
    {
      //  time since start >= length of time intvl
      if ((millis() - msStartTime) >= interval) 
      {
        trigger_action = true;
        // reset start time
        msStartTime = millis();
      }
      else trigger_action = false;
    }
    else trigger_action = false;
  }

  void play()
  {
    if(!playing) playing  = true;
  }

  void pause()
  {
    playing = false;
  }
}
