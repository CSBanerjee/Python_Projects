#class is a blueprint or template. Class name starts with a capital letter
class Student:
  def __init__(self,name,grade,percentage,team): #it is a method of the class
    self.name = name #attribute
    self.grade = grade #attribute
    self.percentage = percentage
    self.team = team
  
  def student_details(self): #it is a method of the class
    print(f"{self.name} is in class {self.grade} with {self.percentage}%")

team1 = 'A'
team2 = 'B'
#object - instance of a class
student1 = Student('Madhav',11,96,team1)
student2 = Student('Vishaka',12,88,team2)

#child class
class GraduateStudent(Student):
  def __init__(self, name, grade, percentage,team,stream):
    super().__init__(name, grade, percentage,team)
    self.stream = stream
  
  def student_details(self):
    return super().student_details() #method inherit from parent class

Grad_Student1 = GraduateStudent('Keshav',12,96,team1,'PCM')
#print(Grad_Student1.stream)
Grad_Student1.student_details()

