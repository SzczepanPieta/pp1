arr=[[-38, 19],[5,40],[-7,11],[29,16]]

min=0
max=0
min_col=0
min_row=0
max_col=0
max_row=0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if min>arr[i][j]:
            min=arr[i][j]
            min_row=i
            min_col=j
        if max<arr[i][j]:
            max=arr[i][j]
            max_row=i
            max_col=j
print(min_row)
print(min_row)
print(min)
print(max_row)
print(max_row)
print(max)