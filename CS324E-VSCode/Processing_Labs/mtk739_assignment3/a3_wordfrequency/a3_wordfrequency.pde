int[] wordFrequency = {};
int[] wordDensity = {};

void setup(){
  //extract data from wordfrequency.txt and store in an array
  String[] wordFrequencyRaw = loadStrings("wordfrequency.txt");
  
  //manipulate data to be in array of ints, wordFrequency and wordDensity
  for (int i = 0; i < wordFrequencyRaw.length; i++){
    String[] separate = split(wordFrequencyRaw[i], ": ");
    wordFrequency = append(wordFrequency, int(separate[0]));
    wordDensity = append(wordDensity, int(separate[1]));
  }
  
  size(510, 665);
  background(0);
  //printArray(wordFrequency);
  //printArray(wordDensity);
}

void draw(){
  color[] colorArray = {color(255, 0, 0), color(255, 165, 0), color(255, 255, 0), color(0, 255, 0), color(0, 0, 255), color(75, 0, 130), color(127, 0, 255)};
  
  float maxY = max(wordDensity);
  for (int i = 0; i < wordFrequency.length; i++){
    stroke(colorArray[(i)%7]);
    strokeWeight(4);
    line(0,i*4,wordDensity[i]*500/maxY+10,i*4);
  }
}
