n = int(input("enter a number :"))
temp = n 
sum_fact = 0
while n>0:
    fact=1
    digit = n%10
    for i in range(1,digit+1):
        fact =fact*i
    sum_fact+=fact
    n=n//10
if sum_fact==temp:
    print("strong number")
else:
    print("not a strong number")