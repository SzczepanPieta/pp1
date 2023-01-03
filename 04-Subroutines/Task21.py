def bmi():
    bemi=0
    y=float(input("Put your Height here in m: "))
    z=float(input("Put your Weight here in kg: "))
    bemi=z/(y**2)
    return bemi

print("Your BMI is:",bmi())



