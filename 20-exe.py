matrix1 = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
matrix2 = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]

def addMatrix(m1, m2):
    if len(m1) != len(m2): return "Invalid numbers of raws"
    for i in range(len(m1)):
        if len(m1[i]) != len(m2[i]): return "Invalid numbers of columns"
    
    r = len(m1)
    c = len(m1[0])
    add = [[0 for j in range(c)] for i in range(r)]
    
    for i in range(r):
        for j in range(c):
            add[i][j] = m1[i][j]+m2[i][j]
    
    return add


matrix = addMatrix(matrix1, matrix2)

for i in matrix:
    print(i)

