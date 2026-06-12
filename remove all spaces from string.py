arr = list(map(int,input("enter array elements:").split()))
duplicates =[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j] and arr[j] not in duplicates:
            duplicates.append(arr[j])
if len(duplicates)==0:
    print("no duplicates")
else:
    print("duplicate elements are:",duplicates)