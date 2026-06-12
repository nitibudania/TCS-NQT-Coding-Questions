def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    mid = (low+high)//2
    while low<=high:
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high = mid-1
    return -1
arr = list(map(int, input("enter list number: ").split()))
target = int(input("enter the target number: "))
position = binary_search(arr,target)
if position == -1:
    print("not found")
else:
    print("the position of the number in the array is :",position)