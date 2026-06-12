n = int(input("enter vlaue of n:"))
arr= list(map(int,input("enter a number till N:").split()))
total_sum=(n*(n+1))//2
arr_sum = sum(arr)
missing_value = total_sum - arr_sum
print("missing number:",missing_value)