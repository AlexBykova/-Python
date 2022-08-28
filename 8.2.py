try:
    a,b = int(input('Введите делимое: ')), int(input('Введите делитель: '))
    print(f'{a}:{b}={a/b}')
except ZeroDivisionError:
    print('На 0 делить нельзя! Одумайтесь! (」°ロ°)」')
except Exception:
    print('Неизвестная ошибка... ╮(￣ω￣;)╭')
except ValueError:
    print('Вы явно ввели что-то не то... Будьте внимательнее! (￢_￢)')