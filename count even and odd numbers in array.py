arr=list(map(int,input("enter elements: ").split()))
even_count=0
odd_count=0
for num in arr:
    if num %2 ==0:
        even_count+=1
    else:
        odd_count+=1
print("number of odds: ",odd_count)
print("number of evens: ",even_count)