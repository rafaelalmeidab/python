class Retangulo:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def setL1(self, l1):
        self.l1 = l1

    def setL2(self, l2):
        self.l2 = l2

    def getArea(self):
        return self.l1*self.l2

    def getPerimeter(self):
        return ((2*(self.l1)) + (2*(self.l2)))

a = Retangulo(2,3)
print("Area: " , a.getArea())
print("Perimetro: " , a.getPerimeter())       
 