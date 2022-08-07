spisok = input('Введите несколько целых чисел через пробел: ')
spisok = spisok.split()
#print(spisok)
res_sp = [int(ob) for ob in spisok]
#print(res_sp)
i=1
if len(res_sp)%2 !=0:
    while i<=len(res_sp)-2:
        res_sp[i],res_sp[i-1]=res_sp[i-1],res_sp[i]
        i+=2
else:
    while i<len(res_sp):
        res_sp[i],res_sp[i-1]=res_sp[i-1],res_sp[i]
        i+=2
print('Список из перевернутых пар: ', res_sp)
