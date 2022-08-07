tov,name,price,quantity,ed=[],[],[],[],[]
i=1
while True:
    q = input('Есть ли у Вас не внесённые в базу товары? (да или нет)---> ')
    if q.lower() == 'да':
        some = {}
        some['Название'] = input('Введите название товара: ')
        some['Цена'] = input('Введите цену товара: ')
        some['Количество'] = input('Введите оставшееся количество товара: ')
        some['ед.изм'] = input('Введите единицу измерения количества товара: ')
        tov.append((i,some))
        i+=1
    elif q.lower() == 'нет':
        break
    else:
        print('Вы ввели что-то не то. Будьте внимательнее!')
print('База Ваших товаров:')
print (tov)

if len(tov)>0:
    for el in tov:
        inf=el[1]
        for key,val in inf.items():
            if key == 'Название':
                name.append(val)
            elif key == 'Цена':
                price.append(val)
            elif key == 'Количество':
                quantity.append(val)
            else:
                ed.append(val)
    analytics={'Названия товаров':name, 'Цены на товары':price, 'Количество каждого товара': quantity, 'Единицы измерения количества товаров':ed}
    print('Анализ Ваших товаров')
    print(analytics)
else:
    print('Ваша база данных пуста. Невозможно сформировать анализ товаров.')
