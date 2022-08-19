def fac (a):
    for el in range(1,a+1):
        res=1
        while el>0:
            res*=el
            el-=1
        yield res

chislo=int(input('Введите число: '))
print(f'Факториалы чисел от 1 до {chislo}:')
for i in fac(chislo):
    print(i)