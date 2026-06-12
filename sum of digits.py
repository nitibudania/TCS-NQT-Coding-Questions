x = int(input("enter a number"))
original = x
total = 0
if x<0:
    x = -x
temp = x
while temp > 0 :
    digit = temp%10
    total = total + digit
    temp = temp//10
    
if original == x:
    total =  total
else:
    total = -total
print("the total number is sum",total)
    

