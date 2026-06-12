rows= int(input("enter the number of rows"))
cols= int(input("enter the number of cols"))
print("enter a elements: ")
A=[]
for i in range(rows):
    row=list(map(int,input().split()))
    while rows !=cols:
        print("invalid enter again")
        row=list(map(int,input().split()))
    A.append(row)
print("transpose of  matrix is:")
for j in range(cols):
    for i in range(rows):
        print(A[i][j],end = " ")
        
