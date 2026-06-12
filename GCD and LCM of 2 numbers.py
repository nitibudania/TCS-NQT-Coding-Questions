def gcd(a,b):

    while b:
        a,b=b,a%b

    return a
x = int(input("enter the first number:"))
y = int(input("enter the second number:"))
g = gcd(x,y)
l = (x*y)//g
print("gcd:",g)
print("lcm:",l)