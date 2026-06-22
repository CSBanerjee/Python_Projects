class Age:
    def __init__(self,yearofbirth:int,currentyear:int):
        self.yearofbirth = yearofbirth
        self.currentyear = currentyear
    
    def message(self):
        difference = abs(self.currentyear-self.yearofbirth)
        plural = '' if difference==1 else 's'
        if self.currentyear<self.yearofbirth:
            return 'You are {} year{} old.'.format(difference,plural)
        elif self.currentyear<self.yearofbirth:
            return 'You will be born in {} year{}.'.format(difference, plural)
        else:
            return 'You were born this very year!'

select = Age(2026,2020)
print(select.message())




