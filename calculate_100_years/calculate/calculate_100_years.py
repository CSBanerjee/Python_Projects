from datetime import datetime 

class Person:
  def __init__(self,name:str, age: int):
    self.name = name 
    self.age = age 
  
  def year_turn_100(self)->int:
    """Calculate the year when this person will turn 100."""
    current_year = datetime.now().year
    years_left = 100- self.age
    year =  current_year + years_left
    message =  f"Hello {self.name}, you will be 100 years old in the year of {year}"
    return message