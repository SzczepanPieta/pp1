def transpose_matrix(m):
    n=len(m)
    z=len(m[0])
    mt=[[0]*n for i in range(z)]
    for i in range(n):
        for j in range(z):
            mt[j][i]=m[i][j]
    return mt

def druk(matrix):
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j],end=" ")
        print()

def mnozenie(macierz,liczba):
    n=len(macierz)
    m=len(macierz[0])
    for i in range(n):
        for j in range(m):
            macierz[i][j]*=liczba

    return macierz


a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3,4,5],[6,7,8,9,0]]

at=transpose_matrix(a)
druk(at)
bt=transpose_matrix(b)
print('************************')
druk(b)
print('************************')
druk(bt)
bt5=mnozenie(bt,5)
druk(bt5)
