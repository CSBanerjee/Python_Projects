class CommonElements:
  def __init__(self,list1,list2):
    self.list1 = list1
    self.list2 = list2
  
  def find_common(self):
    """Return the common elements between two lists."""
    return list(set(set(self.list1) & set(self.list2)))


def main():
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  finder = CommonElements(a,b)
  print(finder.find_common())

if __name__ == "__main__":
  main()


