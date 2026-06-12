n = int(input("enter a number: "))
count = 0
if n == 0 :
    count+=1
else:
    n = abs(n)
    while(n>0):
        count+=1
        n = n//10
print("the number of digit :",count)