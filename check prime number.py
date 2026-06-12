n = int(input("enter a number: "))
count = 2
if n<2:
    print("not a prime number")
else:
    for i in range(2,n):
        if n%i==0:
            count+=1
        
if(count==2):
    print("prime number")
else:
    print("not a prime number ")
            
    