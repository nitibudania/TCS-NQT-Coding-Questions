n = int(input("enter a number :  "))
digit = 0
reverse=0
temp =n
if n<0:
    n=-n
while n>0:
    digit = n%10
    reverse = reverse*10+digit
    n=n//10
if temp<0:
    reverse = -reverse
print(reverse)
