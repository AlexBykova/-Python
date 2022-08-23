with open('no1.txt','w+') as f_obj:
    a=None
    while a!='':
        a=input('Введите информацию для записи в файл. Для окончания ввода нажмите Enter: ')
        print(a,file=f_obj)
    print('Содержимое файла:')
    f_obj.seek(0)
    print(f_obj.readlines())
