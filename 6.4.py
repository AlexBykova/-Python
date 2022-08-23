class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self,direction):
        print(f'Машина завернула - {direction}')

    def show_speed(self):
        print(f'Скорость движения машины = {self.speed}')

class TownCar (Car):
    def show_speed(self):
        if self.speed>60:
            print(f'Скорость движения машины = {self.speed}. Вы превышаете допустимую скорость! Замедлитесь!')
        else:
            print(f'Скорость движения машины = {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed>40:
            print(f'Скорость движения машины = {self.speed}. Вы превышаете допустимую скорость! Замедлитесь!')
        else:
            print(f'Скорость движения машины = {self.speed}')

class PoliceCar(Car):
    pass


a = TownCar(speed=90, color='white', name='Reno Duster')
print(f'Характеристики первой машины: название - {a.name}, цвет - {a.color}, стоит на балансе полиции - {a.is_police}')
a.go()
a.show_speed()
a.turn('вправо')
a.stop()
print()

b = SportCar(speed = 140, color = 'black', name = 'Lexus LFA')
print(f'Характеристики второй машины: название - {b.name}, цвет - {b.color}, стоит на балансе полиции - {b.is_police}')
b.go()
b.show_speed()
b.turn('влево')
b.stop()
print()

c = WorkCar(speed = 40, color = 'green', name = 'Lada Priora')
print(f'Характеристики третьей машины: название - {c.name}, цвет - {c.color}, стоит на балансе полиции - {c.is_police}')
c.go()
c.show_speed()
c.turn('вникуда')
c.stop()
print()

d = PoliceCar(speed = 60, color = 'grey', name = 'Volga 3110',is_police=True)
print(f'Характеристики четвёртой машины: название - {d.name}, цвет - {d.color}, стоит на балансе полиции - {d.is_police}')
d.go()
d.show_speed()
d.turn('внитуда')
d.stop()
print()
