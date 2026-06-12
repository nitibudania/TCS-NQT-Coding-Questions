def leap(x):
    if (x%4 == 0 and x%100 != 0 ) or x%400 == 0:
        print("leap year")
    else:
        print("not a leap year")
x = int(input("enter a year:"))
if (x<0):
    print("invlaid output")
else:
    leap(x)
