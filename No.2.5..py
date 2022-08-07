spisok = input('Введите несколько целых чисел через пробел: ')
spisok = spisok.split()
res_sp = [int(ob) for ob in spisok]
print('Ваш упорядоченный список чисел: ', sorted(res_sp))
per = int(input('Введите еще одно число: '))
res_sp.append(per)
print('Ваш навый упорядоченный список чисел: ', sorted(res_sp))
