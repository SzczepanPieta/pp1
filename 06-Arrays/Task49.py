def transpose_matrix(m):
    n=len(m)
    z=len(m[0])
    mt=[[0]*n for i in range(z)]
    for i in range(n):
        for j in range(z):
            mt[j][i]=m[i][j]
    return mt

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3,4,5],[6,7,8,9,0]]
c=[[5,6,7,8]]

at=transpose_matrix(a)
print(at)
bt=transpose_matrix(b)
print('************************')
ct=transpose_matrix(c)
print(bt)
print('************************')
print(ct)


