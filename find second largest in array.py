def second_largest(arr):
    if len(arr)<2:
        return None
    first = arr[0]
    second = float('-inf')
    for num in arr:
        if num>first:
            second = first
            first = num
        elif num>second and num!=first:
            second = num
    if second == float('inf'):
        return None
    return second
arr = list(map(int, input("enter numbers in the list: ").split()))
second = second_largest(arr)
if second==None:
    print("the second largest number doesnot exist")
else:
    print("the second largest number is : ",second)