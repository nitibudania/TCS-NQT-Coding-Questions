def vc_count(s):
    v=0
    c=0
    vowels = set("aeiouAEIOU")
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v= v+1
            else:
                c=c+1
    print("the number of vowels in string is :",v)
    print("the number of consonant in the string is :",c)
s = input("enter a string : ")
vc_count(s)            





