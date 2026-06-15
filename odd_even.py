#option 1
# num = 6
# if num%2 ==0:
#   print("the number is even")
# else:
#   print("the number is odd")

#option 2 
# def find_odd_even(num):
#   if num%2==0:
#     return "even"
#   else:
#     return "odd"

# num = int(input("Enter a number here: "))
# result = find_odd_even(num)
# print(f"{num} is {result}")

#option 3
class Odd_even:
  def __init__(self,num:int):
    self.num = num
  
  def calculate(self):
    if self.num%2==0:
      return "even"
    else:
      return "odd"
  
abc = Odd_even(5)
result =abc.calculate()
print(result)
