def polsov (**kwargs)->dict:
    print('***')
    print('Общая информация: ', kwargs)

print('Введите данные пользователя: ')

polsov(name=input('Имя: '),surname=input('Фамилия: '),year=input('Год рождения: '),sity=input('Город проживания: '),email=input('Еmail: '),telephon=input('Телефон: '))

