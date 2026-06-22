class ReturnWeekday:
    def __init__(self, num: int=None):
        self.num = num 
  
    def selection(self):
        days = {
                1: "Sunday",
                2: "Monday",
                3: "Tuesday",
                4: "Wednesday",
                5: "Thursday",
                6: "Friday",
                7: "Saturday"
                }
        attempts = 0
        while attempts < 3:
            user = int(input("Please enter a number between 1 to 7: "))
            #user = self.num
            if  1<= user <=7:
                return days[user]
            else:
                attempts += 1
                print(f"Invalid input. Attempts left: {3 - attempts}")
        
        return "Too many invalid attempts. Game Over"


providenumber = ReturnWeekday()
print(providenumber.selection())       


