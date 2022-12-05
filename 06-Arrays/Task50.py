def convertion(m):
    n=len(m)
    z=len(m[0])
    mt=[0]*n*z
    k=-1
    for i in range(n):
        for j in range(z):
            k=k+1
            mt[k]=m[i][j]
            
    return mt

arr=[[2,3],[1,5]]
arr1=[[5,0,3,7,5],[9,0,9,1,2]]
arr2=[[2,1],[3,5],[7,4],[2,6]]

a=convertion(arr)
print(a)
b=convertion(arr1)
print(b)
c=convertion(arr2)
print(c)