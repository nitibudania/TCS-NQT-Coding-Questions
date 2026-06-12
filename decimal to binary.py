n = int(input("enter a number : "))
binary = ""
digits="01"
if n == 0 :
    binary ="0"
else:
    while n>0:
        remainder = n%2
        binary = digits[remainder]+binary
        n=n//2
print("the binary of the given number is :",binary)
