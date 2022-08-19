def zp(vir,stch,prem):
    vir,stch,prem=int(vir),int(stch),int(prem)
    res=(vir*stch)+prem
    return res

from sys import argv
name, a,b,c =argv
print(f'Заработная плата сотрудника составляет: {zp(vir=a,stch=b,prem=c)} рублей')