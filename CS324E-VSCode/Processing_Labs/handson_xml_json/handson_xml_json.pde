// globals
XML test;
XML ebayXML;
JSONArray JSONarr;

// setup and code
void setup()
{
  test = loadXML("test.xml");
  
  println("test.xml's children:");
  for (XML child : test.getChildren()) 
  {
    println(child);
  }
  println();
  
  
  ebayXML = loadXML("ebay.xml");

  println("for ebay.xml, print each listing's seller info:");
  XML[] listings = ebayXML.getChildren("listing"); //<>//
  for (XML listing : listings) 
  {
    println(listing.getChild("seller_info")); //<>//
  }
  println();
  
  
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

}
