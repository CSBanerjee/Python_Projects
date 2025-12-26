import random
def play():
  user = input("What is your choice? 'r' for rock,'p' for paper,'s' for scissor ")
  computer = random.choice(['r','p','s'])
  if user == computer:
    print("It is a tie")
  if is_win(user,computer):
    return "you Won"
  return "you lost"
def is_win(player,opponent):
   if(player == 'r' and opponent == 's') or (player =='s' and opponent =='p' ) \
    or (player == 'p' and opponent =='r'):
        return True

print(play())
  