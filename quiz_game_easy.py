print("Welcome to my computer quiz")
playing = input("Do you want to play? ")
if playing.lower() != 'yes':
  quit()
print("Okay! Lats Play")
score = 0

answer = input("What Does CPU stand for? ")
if answer.lower() == "central processing unit":
  print('correct!')
  score +=1
else:
  print("incorrect!")
answer = input("What Does GPU stand for? ")
if answer.lower() == "graphic processing unit":
  print('correct!')
  score +=1
else:
  print("incorrect!")
answer = input("What Does RAM stand for? ")
if answer.lower() == "random access memory":
  print('correct!')
  score +=1
else:
  print("incorrect!")

print(f"you got {score}")

