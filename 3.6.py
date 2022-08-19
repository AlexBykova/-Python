def int_func(a:str)->str:
    """Функция извлекает первую букву слова, делает её прописной и склеивает слово обратно"""
    m=a[0]
    m=m.upper()
    n=a[1:len(a)]
    return(m+n)

print(int_func(input('Введите слово: ')))
