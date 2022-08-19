my_list=[25,25,14,17,17,19,44,57,69,1,1,2,3,4,4,4,5,6,7,8,9,10,10,11,11,12,12,13,13,13,13,14,15]
print('Исходный список: ',my_list)
new_spisok = [a for a in my_list if my_list.count(a)==1]
print(new_spisok)