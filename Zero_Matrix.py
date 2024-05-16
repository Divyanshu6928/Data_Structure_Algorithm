def zero_matrix(matrix):    
    row=[]
    col=[]
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==0):
                row.append(i)
                col.append(j)

    for k in range(len(row)):
        for i in range(n):
            for j in range(m):
                if(row[k] == i):
                    matrix[i][j]=0

    for k in range(len(col)):
        for i in range(n):
            for j in range(m):
                if(col[k] == j):
                    matrix[i][j]=0