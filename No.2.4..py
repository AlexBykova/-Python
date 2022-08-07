spisok = input('Введите несколько слов через пробел: ')
spisok = spisok.split()
i=1
for sp in spisok:
    if len(sp)>=10:
        print(f'{i}.', sp[:10])
    else:
        print(f'{i}.{sp}')
    i+=1
