class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def getfulname(self):
        ful_name=self.name+' '+self.surname
        return ful_name

    def gettotalincome(self):
        totalincome=self._income['wage'] + self._income['bonus']
        return totalincome

n = input('Введите имя работника: ')
s = input('Введите фамилию работника: ')
p = input('Введите должность работника: ')
zp = int(input('Введите оклад: '))
pr = int(input('Введите премию: '))

p = Position(name = n, surname = s, position = p, wage = zp, bonus = pr)
print()
print(f'Заработная плата работника {p.getfulname()} составляет {p.gettotalincome()}')