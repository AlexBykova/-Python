class Road:

    def __int__(self, length, width):
        self.length=length
        self.width=width

    def weight(self, length, width,mam,sm):
        """метод вычисляет массу асфальта, необходимого для покрытия всей дороги
        length - длина
        width - ширина
        mam - масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см
        sm - число см толщины полотна"""
        massa = length*width*mam*sm
        print(f'Масса асфальта, необходимая для постройки дороки {length} * {width}, с толщиной покрытия {sm}см и массой покрытия на 1 кв.см. {mam}кг = {massa} кг.')


a=Road()
length = int(input('Введите длину дороги: '))
width = int(input('Введите ширину дороги: '))
mam = int(input('Введите массу асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см: '))
sm = int(input('Введите толщину полотна в см: '))
a.weight(length, width,mam,sm)