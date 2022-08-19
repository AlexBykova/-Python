from itertools import count, cycle

a=int(input('Введите начальное число: '))
i=0
k=0
print ('Двадцать последующих чисел (включая данное):')
for el in count(a):
    print(el)
    i+=1
    if i==20:
        break

print('***')
spisok_1=[1,2,3,4,5,6,7,8,9]
print('Исходный список: ',spisok_1)
print('Дублирующий список: ')
for el in cycle(spisok_1):
    print(el)
    k+=1
    if k==2*len(spisok_1):
        break