class ArrestRecords
{
  //fields
  ArrayList<ArrestRecord> records;
  
  //constructor
  ArrestRecords()
  {
    records = new ArrayList<ArrestRecord>();
  }
  
  void addRecord(ArrestRecord r)
  {
    records.add(r);
  }
  
  ArrestRecord getRecord(int id)
  {
    return records.get(id-1);
  }
  
  ArrestRecord removeRecord(int id)
  {
    ArrestRecord r = records.get(id-1);
    records.remove(id-1);
    return r;
  }
  
  
}
