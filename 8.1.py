class Dat:
    def __init__(self,stroka):
        per=stroka.split('-')
        self.day=per[0]
        self.mes=per[1]
        self.god=per[2]

    def __str__(self):
        return f'Дата - {self.day} число {self.mes} месяца {self.god} года'

    @classmethod
    def converterin(cls,yach):
        per=yach.split('-')
        a = [int(per[i]) for i in range(len(per))]
        return f'Дата в виде списка чисел: {a}'

    @staticmethod
    def valid(day,month,god):
        if (0<=day<=31) and (0<=month<=12) and (0<=god<=3000):
            print('Дата введена корректно')
        else:
            print('Дата введена некорректно')



a=input('Введите дату в формате "дд-мм-ггг" -> ')
c=a
b=a.split('-')
b = [int(b[i]) for i in range(len(b))]
Dat.valid(b[0],b[1],b[2])
a=Dat(a)
print(a)
print(Dat.converterin(c))