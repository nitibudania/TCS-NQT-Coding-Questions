n = int(input("enter a number: "))
temp = n
digit  = 0
reverse = 0
while n>0:
    digit = n%10
    reverse = reverse*10+digit
    n = n//10
if reverse == temp:
    print("palindrome")
else:
    print("not a palindrome")