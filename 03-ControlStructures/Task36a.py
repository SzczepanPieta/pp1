n=int(input("Enter a number: "))

ile_pierwsza=0
i=2
while ile_pierwsza<n:
    licznik=0
    for x in range(2,i):
        if i%x==0:
            licznik=licznik+1
    if licznik==0:
        ile_pierwsza=ile_pierwsza+1
        print(i,end=" ")
    i=i+1
    






