s = input("enter string: ")
ch = input("enter character you want to remove from string : ")
result=""
for c in s:
    if c != ch:
        result+=c
print("string after removal: ",result)
    