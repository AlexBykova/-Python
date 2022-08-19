def int_func(*args):
    """Функция вкаждом слове строки извлекает первую букву, делает её прописной, склеивает слово обратно и попутно собирает список из троки"""
    res=[]
    for a in args:
        m=a[0]
        m=m.upper()
        n=a[1:len(a)]
        el=m+n
        res.append(el)
    return res

st=input('Введите строку для преобразования: ')
sl=st.split()
result=int_func(*sl)

print(' '.join(result))
