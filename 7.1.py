class Matrix:
    def __init__(self,osnova):
        self.matrix = osnova

    def __str__(self):
        st=''
        for i in self.matrix:
            for j in i:
                st+=f'  {j} '
            st+='\n'
        return st

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

a = Matrix([[1,2,3],[4,5,6],[7,8,9]])
b = Matrix([[1,2,3],[4,5,6],[7,8,9]])

print('Первая матрица: ')
print(a)
print('Вторая матрица: ')
print(b)
print('Сумма матриц: ')
print(a+b)