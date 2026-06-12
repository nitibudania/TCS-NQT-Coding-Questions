s=input("enter a string")
clean = s.replace(" ","").lower()
reverse = clean[::-1]
if clean == reverse:
    print("string is palindrome")
else:
    print("string is not a palindrome")