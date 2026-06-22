import random
class guessing_game:
  def __init__(self):
    self.num = None
  
  def select_number(self):
    attempts = 0
    while attempts<3:
      self.num = input("Select a number between 1 to 9: ")
      if self.num.isdigit() and 1<=int(self.num)<=9:
        return int(self.num)
      else:
        attempts +=1
        print(f"Invalid choice. Please enter a valid number between 1 to 9. Attempts left: {3 - attempts}")
    print("Too many invalid attempts. Game Over")
    quit()
  
  def selection(self):
    user = self.select_number()
    computer = random.randint(1,9)
    if user == computer:
      return "You won"
    else:
      attempts = 0
      while attempts<3:
        if user>computer:
          return "It is too high"
        else:
          return "It is too low"
        attempts +=1
        return f"remain chances {3-attempts}"
      return "Too many incorrect attempt. Game Over"

if __name__=="__main__":
  getnumber = guessing_game()
  print(getnumber.selection())
      
  
