# arr=list(map(int,input("enter elements:").split()))
# key = int(input("enter element to find freq:"))
# count = 0
# for num in arr:
#     if num==key:
#         count+=1
# print("freq element is:",count)
arr = list(map(int,input("").split()))
freq ={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

print("frequency of each element :")
for key, value in freq.items():
    print(key,":",value)