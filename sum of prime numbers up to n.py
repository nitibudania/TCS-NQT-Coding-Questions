n = int(input("enter a number: "))
sum_prime=0
for num in range(2,n+1):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        sum_prime+=num
print("the sum of all prime numbers is: ",sum_prime)