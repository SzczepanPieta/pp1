def identity_matrix(n):
    for i in range(0, n):
        for j in range(0, n):
            if (i == j):
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print()
      
n = 5
identity_matrix(n)