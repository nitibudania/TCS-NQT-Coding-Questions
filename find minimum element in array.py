arr = list(map(int,input("enter elements: ").split()))
minimum = arr[0]
for num in arr:
    if num<minimum:
        minimum = num
print("the minimum element is :",minimum)