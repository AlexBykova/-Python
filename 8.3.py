class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt
spisok=[]
while True:
    try:
        el=input('Введите число для внесения в список или "fin" для завершения работы программы:')
        if el.isdigit()== True:
            spisok.append(int(el))
        elif el == 'fin':
            break
        elif el!='fin':
            raise MyError('Вы ввели недопустимый символ (눈_눈)')
    except MyError as o:
        print(o)
    else:
        print(f'Ваш список - {spisok}')

print(f'Ваш список - {spisok}')