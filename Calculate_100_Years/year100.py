from datetime import datetime 

class Person:
  def __init__(self,name:str,age:int):
    self.name = name
    self.age = age 
  
  def year_turn_100(self)->int:
    """Calculate the year when this person will turn 100."""
    current_year = datetime.now().year
    years_left = 100 - self.age
    return current_year+years_left
  
  def message(self)->str:
    """Return a personalized message."""
    year = self.year_turn_100()
    return f"Hello {self.name}, you will turn 100 years old in the year {year}."
  



