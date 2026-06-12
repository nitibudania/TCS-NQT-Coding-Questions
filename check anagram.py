def is_anagram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    if sorted(s1)==sorted(s2):
        print("anagram")
    else:
        print("not an anagram")
s1= input("enter a string: ")
s2 = input("enter another string: ")
is_anagram(s1,s2)
