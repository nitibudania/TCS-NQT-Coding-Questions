power = int(input("enter the power: "))
base = int(input("enter the base: "))
result = 1
for i in range(power):
    result = result*base
print("the result is : ",result)