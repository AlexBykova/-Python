import re
res={}
with open('No6.txt','r+',encoding='utf-8') as pred:
    list=pred.readlines()
    for st in list:
        a=st[:st.index(':')]
        match = re.findall(r'\d+',st)
        match = [int(num) for num in match]
        summa = sum(match)
        res[a]=summa
    print ('Полученная из файла информация по дисциплинам:')
    print (res)
