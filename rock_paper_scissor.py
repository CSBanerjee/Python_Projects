import random 

class RPS:
  def __init__(self):
    self.choices = ['r','p','s']
  
  def get_user_choice(self):
    attempts = 0
    while attempts<3:
      user = input("What is your choice (r/p/s): ").lower()
      if user in self.choices:
        return user
      else:
        attempts +=1
        print(f"Invalid choice. Please enter r, p or s. Attempts left: {3 - attempts}")
    print("Too many invalid attempts. Game Over")
    quit()
  
  def selection(self):
    user = self.get_user_choice()
    computer = random.choice(self.choices)
    print(f"Computer chose: {computer}")
    if user ==computer:
      print("It is a tie")
    elif self.is_win(user,computer):
      print("You Won!")
    else:
      print("You loose")
  
  def is_win(self,player,opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')


if __name__=="__main__":
  game = RPS()
  game.selection()