class Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
  def annual_salary(self):
     return self.salary * 12 

class Manager(Employee):
    def __init__(self, name, salary,bonus):
       super().__init__(name, salary)
       self.bonus = bonus
    
    def annual_salary(self):
       return super().annual_salary()+self.bonus 

m = Manager("Ravi",6000,1000)
print(m.annual_salary())