from time import sleep

class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        i=0
        while i!=3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(9)
            i+=1

a = TrafficLight()
a.running()