season = {'Зима':[1,2,12], 'Весна':[3,4,5], 'Лето':[6,7,8], 'Осень':[9,10,11]}
num = int(input('Введите любое целое число от 1 до 12: '))
for key,val in season.items():
    a,b = key,val
    if num in val:
        print('Выбранное Вами время года:', key)