def two_dim_into_1D(array):
    arr=[0]*len(array) *len(array[0])
    l=-1
    for i in range(len(array)):
        for j in range(len(array[0])):
            l+=1
            arr[l]=array[i][j]
    return arr

def wypisz(array):
    for i in range(len(array)):
            print(array[i],end=" ")
        

wypisz(two_dim_into_1D([[2,3,4,5],[5,6,7,8]]))