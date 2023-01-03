def min(array):
    min=0
    min_i=0
    min_j=0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]<min:
                min=array[i][j]
                min_i=i
                min_j=j

    return min,min_i,min_j

def max(array):
    max=0
    max_i=0
    max_j=0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]>max:
                max=array[i][j]
                max_i=i
                max_j=j
    return max,max_i,max_j



arr=[[-38, 19], [5,40],[-7,11],[-929,16]]



el_max,imax,jmax=max(arr)
print(f"max:",{el_max},"i:",{imax},"j:",{jmax})

el_min,imin,jmin=min(arr)
print(f"min:",{el_min},"i:",{imin},"j:",{jmin})


