def sum(tup):
    elem = (int(a) for a in tup if a!=' ')
    sum=0
    for a in elem:
        sum+=a
    return sum
b=0
ud=None

while True:
    a = input('Введите через пробел числа для суммирования или букву "f" для завершения работы программы: ')
    if a.find('f')==-1:
        b = b + sum(a)
        print('Сумма чисел = ', b)
    else:
        ud=a.find('f')
        a=a.replace(a[ud],' ')
        b = b + sum(a)
        print('Сумма чисел = ', b)
        break





