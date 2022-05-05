class ArrestRecord
{
  //fields
  int ID, year, age, nChecks;
  String race, sex;
  boolean released, employed, citizen;
  
  //constructor
  ArrestRecord(int _ID, boolean _released, String _race, int _year, int _age, 
               String _sex, boolean _employed, boolean _citizen, int _nChecks)
  {
    this.ID = _ID;
    this.released = _released;
    this.race = _race;
    this.year = _year;
    this.age = _age;
    this.sex = _sex;
    this.employed = _employed;
    this.citizen = _citizen;
    this.nChecks = _nChecks;
  }
  
  @Override
  public String toString() 
  {
      return String.format(ID+", "+released+", "+race+", "+year+", "+age+", "+sex+", "+employed+
                           ", "+citizen+", "+nChecks);
  }
  
  
}
