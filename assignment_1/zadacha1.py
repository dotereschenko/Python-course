def diagonalSum(mat):
    sum = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i == j or (i + j + 1) == len(mat):
                sum += mat[i][j]
    return sum
                
