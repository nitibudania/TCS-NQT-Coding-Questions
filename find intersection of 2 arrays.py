arr1 = list(map(int,input("enter elements: ").split()))
arr2 = list(map(int,input("enter elements: ").split()))
intersection=[]
for num in arr1:
    if num in arr2 and num not in intersection:
        intersection.append(num)
print("the intersection of the arrays: ",intersection)