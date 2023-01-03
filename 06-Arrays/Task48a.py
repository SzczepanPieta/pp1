def identity_matrix(n):
    arr=[[0]*n for z in range(n)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i==j:
                arr[i][j]=1
    return arr

def wypisz(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j],end=" ")
        print()

wypisz(identity_matrix(3))
wypisz(identity_matrix(5))
wypisz(identity_matrix(8))