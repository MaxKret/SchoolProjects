/*
Arrests.csv:
"id","released","race","year","age","sex","employed","citizen","checks"
"1","Yes","White",2002,21,"Male","Yes","Yes",3
"2","No","Black",1999,17,"Male","Yes","Yes",3
"3","Yes","White",2000,24,"Male","Yes","Yes",3
"4","No","Black",2000,46,"Male","Yes","Yes",1
"5","Yes","Black",1999,27,"Female","Yes","Yes",1
"6","Yes","Black",1998,16,"Female","Yes","Yes",0
"7","Yes","White",1999,40,"Male","No","Yes",0
"8","Yes","White",1998,34,"Female","Yes","Yes",1
"9","Yes","Black",2000,23,"Male","Yes","Yes",4
"10","Yes","White",2001,30,"Male","Yes","Yes",3
...
*/
// globals
Table table;
ArrestRecords recordTable;

// setup and code
void setup()
{
  table = loadTable("Arrests.csv", "header");
  recordTable = new ArrestRecords();
  
  println(table.getRowCount() + " total rows in table");

  for (TableRow row : table.rows()) 
  {
    int record_id = row.getInt("id");
    recordTable.addRecord(new ArrestRecord(record_id, row.getString("released").equals("Yes"), 
                          row.getString("race"), row.getInt("year"), row.getInt("age"), 
                          row.getString("sex"), row.getString("employed").equals("Yes"), 
                          row.getString("citizen").equals("Yes"), row.getInt("checks")));
    
    //println(recordTable.records.get(record_id-1)); //<>//
  }
  
  // testing of ArrestRecords Methods
  println("first 3 records:");
  println("id,released,race,year,age,sex,employed,citizen,number of checks:");
  //                                   getRecord(int id); id == index+1
  for(int i=1;i<4;i++) println(recordTable.getRecord(i));
  println("removed: "+recordTable.removeRecord(2));
  println("first 3 records:");
  println("id,released,race,year,age,sex,employed,citizen,number of checks:");
  for(int i=1;i<4;i++) println(recordTable.getRecord(i));
  
  
}
