money=int(input("Enter the amount in the PLN: "))

print(f"The amount of PLN {money} in coins:")

ilosc5=money/5

x=int(ilosc5)

print(f"5 zl - {x}")

reszta=money%5

ilosc2=reszta/2

y=int(ilosc2)

print(f"2 zl - {y}")

reszta2=reszta%2

ilosc1=reszta2/1

z=int(ilosc1)

print(f"1 zl - {z}")



