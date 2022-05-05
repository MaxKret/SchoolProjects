//globals
String path = "C:\\Users\\Crackhead\\Desktop\\College Stuff\\CS324E\\Processing_Labs\\";
String[] lines;
PrintWriter output;

//setup
void setup()
{
  
  lines = loadStrings("mytext.txt");
  output = createWriter("words.txt");
  noLoop();
}

//draw
void draw()
{
  for (int i=0; i<lines.length; i++)
  {
    println("length of line: "+str(lines[i].length()));
    String[] subwords = split(lines[i], ' ');
    println("individual words: "+str(subwords.length));
    for(int j=0;j<subwords.length;j++)
    {
      output.println(subwords[j]);
    }
  }
    output.flush();
  output.close();
}
