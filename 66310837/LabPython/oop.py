class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    # def show(self):
    #     print(self.num,"/",self.den)

    # Override
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = Fraction.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
    
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return Fraction.gcd(b, a%b)

# myfraction = Fraction(3, 5)
# myfraction.show()

f1 = Fraction(1, 4)
f2 = Fraction(1, 4)
f3 = f1 + f2
isequals = f1 == f2
print(f3)
print(isequals)