a=str("0805")

b=input("Enter the PIN code: ")



for i in range(2):    
    if b!=a:
        print("Incorect...")
        b=input("Enter the PIN code: ")

if b==a:
    print("Your card is unlocked")

if b!=a:
    print("Incorect...")
    print("Your card is blocked")


