
class Numberz:
    def __init__(self,one=1,two=2):
        self.one = one
        self.two = two

        self.dic = {'One':self.one,
                    'Two':self.two}

ch = Numberz()


ch.one = 5

setattr(ch, 'one', 5)

print(ch.one) 


