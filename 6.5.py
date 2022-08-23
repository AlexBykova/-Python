class Stationery:
    def __init__(self,title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} - Красиво рисует синеньким')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} - Серо-чёрную линию легко стереть')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} - Чёрную черту и черти чистить чураются')


a=Stationery('Письменная принадлежность')
a.draw()

b=Pen('ручка')
b.draw()

c=Pencil('карандаш')
c.draw()

d=Handle('маркер')
d.draw()