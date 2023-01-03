def transpose_matrix(m):
    arr=[[0]*len(m) for z in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            arr[j][i] = m[i][j]
    return arr

def wypisz(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j],end=" ")
        print()

wypisz(transpose_matrix([[2,3,4,5],[5,6,7,8]]))