arr = list(map(int,input("enter elements:").split()))
sorted_array = True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        sorted_array = False
        break
if sorted_array:
    print("array is sorted")
else:
    print("array is not sorted")
