my_list=[1500, 6000, 1, 34, 4, 5, 6, 66, 7, 4, 99, 0, 3, 52, 1]
print('Исходный список: ', my_list)
new_list=[my_list[i] for i in range(1, len(my_list)) if my_list[i]>my_list[i-1]]
print('Новый список: ', new_list)