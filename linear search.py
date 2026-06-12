def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = list(map(int , input("enter numbers: ").split()))
target = int(input("enter a number you want to search: "))
pos = linear_search(arr,target)
if pos == -1:
    print("the  number you want to search is not present")
else:
    print("the position is ",pos)


    