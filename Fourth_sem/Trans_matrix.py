# Напишите функцию для транспонирования матрицы

def transpone_matrix(matrix1):
    trans_matrix = [[0 for j in range(len(matrix1))] for i in range(len(matrix1[0]))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            trans_matrix[j][i] = matrix1[i][j]
    return trans_matrix

def print_matrix(matrix1):
    for i in matrix1:
        print(i)

mx = [[1, 2], [3, 4], [5, 6]]
trans_mx = transpone_matrix(mx)
print_matrix(mx)
print_matrix(trans_mx)
