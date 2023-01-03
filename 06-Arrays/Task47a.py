arr=[[2,3,4,5,6],[7,8,9,10,11],[0,0,0,0,0]]

def wypisz(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=" ")
        print()

wypisz(arr)

def swap(array):
    for i in range(len(array)):
        a=array[i][0]
        b=array[i][-1]
        array[i][0]=b
        array[i][-1]=a

print()
swap(arr)
wypisz(arr)

