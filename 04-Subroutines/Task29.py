def power(x,n):
    if n == 0:
        return x
    return power(x*x,n-1)

print(power(5,2))