with open ('No3.txt','r', encoding="utf-8") as doc:
    a=doc.readlines()
    doc.seek(0)
    zp = 0
    print('Сотрудники с ЗП до 20 000: ')
    for el in a:
        for b in range(len(el)):
            if el[b] == ' ':
                num=float(el[b+1:len(el)-1])
                if num <20000:
                    print(el[:b])
                zp+=num
    print()
    print("Средняя величина ЗП сотрудников = {:8.3f}".format(zp/len(a)))
