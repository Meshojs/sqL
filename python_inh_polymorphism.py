class Area : 
    def __init__(self , l) -> None:
        self.l = l

class Square(Area) : 
    def __init__(self,l,name) -> None:
        self.name = name
        super().__init__(l)
    def calc(self): 
        return self.l * self.l
    def show_name(self) -> str: 
        return "your name is " + self.name 
    
class Rec(Area) : 
    def __init__(self, l , width) -> None:
        self.width = width
        super().__init__(l)
    def calc(self): 
        return self.l * self.width
    
squareOne = Square(10 , "Cute Square")
rec = Rec(20 , 10) 

calc_Method = [squareOne,  rec]
for c in calc_Method : 
    print(c.calc())
 