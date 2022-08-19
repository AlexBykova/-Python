def my_func(a,b,c):
    """Данная функция считает сумму двух наибольших чисел из трёх введённых"""
    sum=0
    chisla=[a,b,c]
    chisla=sorted(chisla)
    sum=chisla[1]+chisla[2]
    return sum

print('Введите три различных числа:')
a,b,c=int(input(' a = ')), int(input(' b = ')), int(input(' c = '))
print('Cумма больших двух равна: ', my_func(a,b,c))


