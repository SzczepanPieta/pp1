def create_2d_arr(x,y):
    arr = []
    for i in range(x):
        arr.append([])
        for j in range(y):
            arr[i].append(0)
    return arr
        
    



def create_2d_array(x,y):
    arr=[[1]*y for i in range(x)]
    return arr 

print(create_2d_arr(3,5))