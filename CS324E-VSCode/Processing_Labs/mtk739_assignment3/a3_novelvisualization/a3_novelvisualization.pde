String[] wordsToDisplay;
color[] colorSet;
String enteredString = "";
String[] currentStrings;

//Sets the colors and loads words from text
public void setup() {
  size(600, 700);
  wordsToDisplay = loadStrings("uniquewords.txt");
  color one = #955050;
  color two = #955091;
  color three = #54DB79;
  color[] colors = {one, two, three};
  colorSet = colors;
  currentStrings = wordsToDisplay;
  mousePressed();
}


public void draw() {
}

//Event Listener for mousePresses, reloads the words when mouse is pressed
public void  mousePressed() {
  gatherWords();
  clear();
  float nextWidth = 0;
  int stringIndex = 0;
  int heightMarker = 20;
  while (heightMarker < 690) {
    int widthMarker = 0;
    while (widthMarker < 580 - nextWidth) {
      if (stringIndex+ 2 >= currentStrings.length) {
        stringIndex = 0;
      }
      fill(colorSet[int(random(0, 3))]);
      stringIndex += 1;
      try {
        text( currentStrings[stringIndex], widthMarker, heightMarker);
        widthMarker += textWidth(currentStrings[stringIndex]+ 5);
        nextWidth = textWidth(currentStrings[stringIndex + 1] + 5);
      }
      catch(Exception e) {
        keyCode = RETURN;
        keyPressed();

      }
    }
    heightMarker += 30;
  }
}

//Changes the enteredString to match user input
public void keyPressed() {
  if (keyCode == ENTER || keyCode == RETURN) {
    enteredString = "" ;
    currentStrings = wordsToDisplay;
    clear();
    
    mousePressed();
  } else {
    enteredString += key;
  }
  gatherWords();
  mousePressed();
}

//Ensures all words match enteredString
public void gatherWords() {
  StringList newArray = new StringList();
  for (int i = 0; i < currentStrings.length; i++) {
    String indexed = currentStrings[i];
    if (indexed.contains(enteredString)) {
      newArray.append(indexed);
      if (random(1)< .1) {
        newArray.shuffle();
      }
    }
  }
  if (newArray.array().length > 0) {
    currentStrings = newArray.array();
  }
}
