with open('No5.txt','w+',encoding='utf-8') as doc:
    print(input('Введите числа через пробел: '),file=doc)
    doc.seek(0)
    i=0
    sum=0
    a=doc.read()
    list=a.split(' ')
    list=[int(list[i]) for list[i] in list]
    for num in list:
        sum+=num
    print('Сумма введённых чисел =', sum)