class Calculators:
    def __init__(self, first_number=0, second_number=0):
        self.first_number = first_number
        self.second_number = second_number 
  #aggregation
    def aggregation(self):
        num1 = input("Insert your first number: ")
        if num1.isdigit():
            num1 = int(num1)
        else:
            print("Input number not valid!")
            return
        num2 = input("Insert your second number: ")
        if num2.isdigit():
            num2 = int(num2)
        else:
            print("Input number not valid!")
            return
        value = num1 + num2 
        print("Sum is:", value)
  #subtraction
    def subtraction(self):
        num1 = input("Insert your first number: ")
        if num1.isdigit():
            num1 = int(num1)
        else:
            print("Input number not valid!")
            return
        num2 = input("Insert your second number: ")
        if num2.isdigit():
            num2 = int(num2)
        else:
            print("Input number not valid!")
            return
        value = num1 - num2 
        print("Total is:", value)


x = Calculators()   # no arguments needed
x.subtraction()     # no arguments passed2
