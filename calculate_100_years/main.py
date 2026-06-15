from calculate.calculate_100_years import Person
def main():
  name = input("Enter your name: ")
  age = int(input("Enter your age: "))
  #Create a person object
  person = Person(name, age)
  print(person.year_turn_100())

if __name__  =="__main__":
  main()