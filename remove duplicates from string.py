def remove_dup(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    print("the new string after removing the duplicates is :",result)
s = input("enter the string: ")
remove_dup(s)