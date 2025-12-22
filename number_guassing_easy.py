import random 
top_of_range = input(f"type a number: ")

if top_of_range.isdigit():
  top_of_range = int(top_of_range)
  if top_of_range <=0:
    print("please time a number more then 0")
    quit()
else:
  print("please provide a valid number next time!")
  quit()


r = random.randrange(top_of_range)

while True:
  user_guess = input("make a guess: ")
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print("please provide a valid number next time!")
    continue
  if user_guess == r:
    print("You guessed it correctly")
    break
  elif user_guess >r:
    print("you guesssed it high")
  else:
    print("you guessed it low")
    
  




