n = int(input("enter a number: "))
if n<1:
    print("fact is not available")
else:
    fact = 1
    for i in range(1,n+1):
        fact*=i
print(fact)
