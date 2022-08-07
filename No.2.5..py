spisok = input('Введите несколько целых чисел через пробел: ')
spisok = spisok.split()
res_sp = [int(ob) for ob in spisok]
res_sp = sorted(res_sp)
print('Ваш упорядоченный список чисел: ', res_sp)
per = int(input('Введите еще одно число: '))
i=0
for num in res_sp:
    if num<=per:
        i+=1
    else:
        break
res_sp.insert(i,per)
print('Ваш навый упорядоченный список чисел: ', res_sp)
