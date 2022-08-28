class Complexnum:
    def __init__(self,re,im):
        self.re=re
        self.im=im

    def __str__(self):
        return f'Комплексное число {self.re}+{self.im}i'

    def __add__(self, other):
        return Complexnum(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complexnum((self.re * other.re - self.im*other.im), (self.im*other.re + self.re*other.im))


a=Complexnum(2,3)
print(a)
b=Complexnum(4,5)
print(b)

print(f'({a}) + ({b}) = {a+b}')
print(f'({a}) * ({b}) = {a*b}')