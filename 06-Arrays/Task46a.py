def change(array):
    a=array[0]
    b=array[-1]

    array[0]=b
    array[-1]=a
    return array

arr=[[2,3,4,5,6],[7,8,9,10,11],[0,0,0,0,0]]

print(arr)

print(change(arr))

    

