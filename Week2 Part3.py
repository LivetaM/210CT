def creating_Matrix(r, c, N): #r - stands for number of row, c - stands for number of columns
    matrixN = []
    for x in range(r):
        row = []
        for y in range(c):
            row.append(N)
        matrixN.append(row)
    return (matrixN)
    
def addition(r, c, N):
    Bmatrix = creating_Matrix(r, c, N)
    Cmatrix = creating_Matrix(r, c, N)
    A = [[0] * r for i in range(c)]
    for row in range(len(Bmatrix)):
        for column in range (len(Cmatrix[row])):
            A[row][column] = Bmatrix[row][column] + Cmatrix[row][column]
    return (A)

def multiplication(r, c, N):
    Bmatrix = creating_Matrix(r, c, N)
    Cmatrix = creating_Matrix(r, c, N)
    A = [[0] * r for i in range(c)]
    for row in range(len(Bmatrix)):
        for column in range (len(Cmatrix[row])):
            for row2 in range (len(Bmatrix[0])):
                A[row][column] = A[row][column] + (Bmatrix[row][row2] * Cmatrix[row2][column])
    return (A)


def final(r, c, N):
    Bmatrix = creating_Matrix(r, c, N)
    Cmatrix = creating_Matrix(r, c, N)
    multi = multiplication(r, c, N)
    add = addition(r, c, N)
    A = [[0] * r for i in range(c)]
    for row in range(len(Bmatrix)):
        for column in range (len(Cmatrix[row])):
            A[row][column] = multi[row][column] - 2*add[row][column]
    return (A)
print (final(3, 3, 2))
    

# addition reference: http://stackoverflow.com/questions/19897212/adding-two-matrices-in-python


