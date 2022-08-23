import json
res={}
with open('No7.txt', 'r', encoding='utf-8') as firms:
    ob_prib=0
    sr_prib=0
    list = firms.readlines()
    for st in list:
        st=st.split()
        fir=st[0]
        pribil=int(st[2])-int(st[3])
        if pribil>0:
            ob_prib=ob_prib+pribil
            res[fir] = pribil
            print(f'Прибыль компании {fir} = {pribil}')
        else:
            a=str(pribil)+'(damage)'
            res[fir] = a
            print(f'Прибыль компании {fir} = {a}')
    print()
    sr_prib=ob_prib/len(list)
    res['average_profit']=sr_prib
    with open("my_fileno7.json", "w") as write_f:
        json.dump(res, write_f)