a,b=int(input('Введите делимое: ')),int(input('Введите делитель: '))
result = lambda delimoe,delitel: delimoe/delitel if delitel!=0 else 'На 0 делить нелья'
print ('Результат деления: ',result(a,b))