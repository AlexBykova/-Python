num=int(input('Введите целое положительное число: '))
res=0
while num>0:
    p=num%10
    if p>res:
        res=p
    num=num//10
print('Максимальная цифра Вашего числа: ',res)
