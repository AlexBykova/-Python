with open('No2.txt','r+') as f_obj:
    a=f_obj.readlines()
    print(f'Количество строк в документе = {len(a)}')
    f_obj.seek(0)
    par = 1
    for el in a:
        kol=1
        for b in range(len(el)):
            if el[b]==' ':
                kol+=1
        print(f'Количество слов в {par}-ой строке документа = {kol}')
        par+=1
