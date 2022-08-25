from abc import abstractmethod, ABC

class Clothes(ABC):
    @abstractmethod
    def rashod(self):
        pass

class coat(Clothes):
    def __init__(self,size):
        self.size = size

    def __str__(self):
        return f"Заказано пальто размером - {self.size}."

    @property
    def rashod(self):
        return (self.size/6.5+0.5)

class suit(Clothes):
    def __init__(self,height):
        self.height = height

    def __str__(self):
        return f"Заказан костюм на рост - {self.height}м."

    @property
    def rashod(self):
        return (2*self.height + 0.3)

a=coat(56)
print(a)

b=suit(1.98)
print(b)
print()

print('Расход ткани на пальто составляет: {:7.3f}'.format(a.rashod))
print('Расход ткани на костюм составляет:{:7.3f}'.format(b.rashod))
print('Общий расход ткани на пошив: {:7.3f}'.format(a.rashod+b.rashod))