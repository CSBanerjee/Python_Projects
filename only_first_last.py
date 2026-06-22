class FirstLastOnly:
  def __init__(self,list:list):
    self.list = list 
  
  def selection(self):
    final_list = []
    final_list.append(self.list[0])
    final_list.append(self.list[-1])
    return final_list

a = [5, 10, 15, 20, 25]

if __name__=="__main__":
  show = FirstLastOnly(a)
  print(show.selection())