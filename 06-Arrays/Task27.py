arr1=[4,36,12,28,9,44,5]
arr2=[5,1,36]

for i in range(len(arr1)):
    hit=0
    for j in range(len(arr2)):
        if arr1[i]!=arr2[j]:
            hit=hit+1
            if hit==len(arr2):
                print(arr1[i])
            
