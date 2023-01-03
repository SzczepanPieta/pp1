x=int(input("Put first cordinate: "))
y=int(input("Put second cordinate: "))

print(f"x={x}")
print(f"y={y}")

if x>=0 and y>=0:
    print(f"Point P{x,y} is in the first quadrant of the coordinate system")

if x>=0 and y<=0:
    print(f"Point P{x,y} is in the second quadrant of the coordinate system")

if x<=0 and y<=0:
    print(f"Point P{x,y} is in the third quadrant of the coordinate system")

if x<=0 and y>=0:
    print(f"Point P{x,y} is in the fourth quadrant of the coordinate system")

if x==0 and y==0:
    print(f"Point P{x,y} is in the middle of the coordinate system")