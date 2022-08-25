class Cell:
    def __init__(self,part):
        self.part=part

    def __str__(self):
        return f"Клетка с количеством ячеек = {self.part}"

    def __add__(self, other):
        return Cell(self.part + other.part)

    def __sub__(self, other):
        if (self.part - other.part)>0:
            return Cell(self.part - other.part)
        else:
            print ('Выполнение данной операции невозможно')

    def __mul__(self, other):
        return Cell(self.part * other.part)

    def __truediv__(self, other):
        return Cell(self.part // other.part)

    def make_order(self,row):
        a = self.part//row
        res = ''
        m = self.part
        if self.part % row != 0:
            for i in range(a + 1):
                if m >= (self.part // a):
                    res = res + ('*' * (self.part // a)) + '/n '
                    m = m - (self.part // a)
                else:
                    res = res + ('*' * m) + '/n '
        else:
            for i in range(a + 1):
                if m >= (self.part // a):
                    res = res + ('*' * (self.part // a)) + '/n '
                    m = m - (self.part // a)
        print (f'Организация ячеек в клетке по рядам осуществляется по схеме: {res}')


a = Cell(7)
print(a)
b = Cell(3)
print(b)
print()

print('Суммой является:', a+b)
print('Разностью является:', a-b)
print('Произведением является:', a*b)
print('Частным является:', a/b)
print()

c = Cell(21)
print(c)
c.make_order(3)