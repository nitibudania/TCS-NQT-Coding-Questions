x = int(input("enter a number:"))
if x<0:
    print("entered number is not an armstrong number")
else:
    original = x
    temp = x
    total = 0
    count = len(str(x))
while temp>0:
    digit = temp % 10
    total = total + digit**count
    temp = temp // 10
if total == original :
    print("an armstrong number")
else:
    print("not an armstrong number")
