class warehouse:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f'Позиция на складе - {self.name}'

class Officeequipment(warehouse):
    def __init__(self, name, energy, price):
        self.name=name
        self.energy=energy
        self.price=price
        self.some={'Название': {self.name}, 'Энергопотребление': {self.energy}, 'Цена': {self.price}}
        self.store=[]
        self.store_all=[]

    def __str__(self):
        return f'Позиция на складе - {self.name}. Характеристики: энергопотребление - {self.energy} Ватт, цена - {self.price}р.'

    def reception(self):
        while True:
            try:
                obj= input(f'Введите наименование: ')
                obj_e = int(input(f'Введите энергопотребление: '))
                obj_p = int(input(f'Введите цену: '))
                ob = {'Название': obj, 'Энергопотребление': obj_e, 'Цена': obj_p}
                self.some.update(ob)
                self.store.append(self.some)
                print(f'Текущий список -\n {self.store}')
            except:
                return f'Данные введены некорректно ╮(￣ω￣;)╭'

            ex=input(f'Для продолжения работы с базой данных нажмите - Enter, для выхода - клавишу "f": ')
            if ex == 'F' or ex == 'f':
                self.store_all.append(self.store)
                print(f'Перечень оборудования:\n {self.store_all}')
                return f'Завершение работы с базой склада'
            else:
                return Officeequipment.reception(self)

class printer(Officeequipment):
    def __init__(self, name, energy, price,fast):
        self.name=name
        self.energy=energy
        self.price=price
        self.fast=fast

    def __str__(self):
        return f'Позиция на складе - {self.name}. Тип - принтер. Характеристики: энергопотребление - {self.energy} Ватт, цена - {self.price}р., скорость печати - {self.fast} листов в минуту'


class scanner(Officeequipment):
    def __init__(self, name, energy, price, scanday):
        self.name = name
        self.energy = energy
        self.price = price
        self.scanday = scanday

    def __str__(self):
        return f'Позиция на складе - {self.name}. Тип - сканер. Характеристики: энергопотребление - {self.energy} Ватт, цена - {self.price}р., максималльное число сканирований - до {self.scanday} сканирований в день'


class xerox(Officeequipment):
    def __init__(self, name, energy, price,maxkop):
        self.name = name
        self.energy = energy
        self.price = price
        self.maxkop = maxkop

    def __str__(self):
        return f'Позиция на складе - {self.name}. Тип - ксерокс в составе МФУ. Характеристики: энергопотребление - {self.energy} Ватт, цена - {self.price}р., max число копий за цикл - {self.maxkop} листов'



a=Officeequipment('Настольная лампа', 75, 1500)
print(a)
print()
b=printer('Zebra ZD420-HC ZD42H43-D0EE00EZ', 240, 26500, 500)
print(b)
print()
c=scanner('Canon image Formula DR-C225 II', 12, 47700, 1500)
print(c)
print()
d=xerox('МФУ лазерное Pantum M6500', 495, 10000, 100)
print(d)
print()
print(a.reception())