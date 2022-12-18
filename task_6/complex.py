from math import sqrt


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, c):
        return self.a == c.a and self.b == c.b

    def __str__(self):
        if self.b >= 0:
            return str(self.a)+ '+' +str(self.b)+'i'
        else:
            return str(self.a) + str(self.b)+'i'

    def abs(self):
        return sqrt(self.a**2 + self.b**2)

    def add(self, c):
        return Complex(self.a + c.a, self.b + c.b)

    def sub(self, c):
        return Complex(self.a - c.a, self.b - c.b)

    def mul(self, c):
        return Complex(self.a*c.a - self.b*c.b,
                       self.b*c.a + self.a*c.b)

    def div(self, c):
        d = c.a*c.a + c.b*c.b
        return Complex((self.a * c.a + self.b * c.b)/d,
                        (self.b * c.a - self.a * c.b)/d)
