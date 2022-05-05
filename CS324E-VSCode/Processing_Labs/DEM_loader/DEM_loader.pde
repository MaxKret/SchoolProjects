// globals
JSONArray JSONarr;
PShape TIN;

// setup and code
void setup()
{
  size(600,600);
   //<>// //<>//
  JSONarr = loadJSONArray("array-01.json");
  int[] arr = new int[JSONarr.size()];
  for (int i = 0; i < JSONarr.size(); i++) 
  {
    arr[i] = JSONarr.getInt(i);
  }
  println("JSON Array:");
  println(JSONarr);
  println("New Array:");
  println("["+arr[0]+", "+arr[1]+", "+arr[2]+", "+arr[3]+", "+arr[4]+"]");
  
  TIN = createShape(); //<>//
  TIN.beginShape(TRIANGLE_STRIP);
  TIN.fill(0, 0, 255);
  for(int i = 0;i<arr.length;i++)
  {
    TIN.vertex(arr[i],arr[i]+i*10);
  }
  TIN.endShape();
}

void draw()
{
  shape(TIN);
}
