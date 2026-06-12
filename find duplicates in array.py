arr = list(map(int,input("").split()))
result = []
count = 0
for num in arr:
    if num!= 0 :
        result.append(num)
    else:
        count+=1
for i in range(count):
    result.append(0)
print("the updated arr:",result)
