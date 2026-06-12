arr = list(map(int,input("enter elements: ").split()))
target = int(input("enter target sum: "))
found = False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print("pair found: ",arr[i],arr[j])
            found = True
            break
    if found:
        break
if not found:
    print("no pair found")
