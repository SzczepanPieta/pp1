def keypad():
    x=1
    while x <=9:
        print(x, end=" ")
        if (x%3)==0:  
            print() 
        x=x+1      
keypad()