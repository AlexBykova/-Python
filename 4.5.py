from functools import reduce
def umn(a,b):
    return a*b

spisok=[a for a in range(100,1001) if a%2==0]
print('Чётные числа от 100 до 1000:')
for a in spisok:
    print(a)
print('Произведение всех элементов списка = ', reduce(umn,spisok))
