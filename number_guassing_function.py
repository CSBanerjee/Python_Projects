import random 
def guess(x):
  random_number = random.randrange(0,x)
  guess_number = 0
  while guess_number !=random_number:
    guess_number = int(input(f"Guess a number between 1 and {x}: "))
    
    if guess_number > random_number:
      print("you are high")
    else:
      print("you are low")
  print("you are correct!")
guess(10)
