class  Arearec:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def calculate_area(self):
        return self.l * self.b
area1 = Arearec(2,7)
area2 = Arearec(3,6)
print(area1.calculate_area())