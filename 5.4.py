d={'One':'Единица','Two': 'Двойка', 'Three': 'Тройка', 'Four': 'Четвёрка'}
with open ('No4.txt','r', encoding="utf-8") as text:
    with open ('No4.rem.txt','w+',encoding='utf-8') as new:
        for line in text:
            for b in range(len(line)):
                if line[b] == ' ':
                    word=(line[:b])
                    i=1
                    for key,val in d.items():
                        if word==key:
                            zam=val+'-'+str(i)
                            print(zam,file=new)