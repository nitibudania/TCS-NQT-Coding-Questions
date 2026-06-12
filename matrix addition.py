rows1=int(input("enter the number of rows for first matrix:"))
cols1=int(input("enter the number of cols for first matrix:"))
print("enter first matrix:")
A=[]
for i in range(rows1):
    row=list(map(int, input().split()))
    while len(row)!=cols1:
        print("invlaid input enter again")
        row=list(map(int, input().split()))
    A.append(row)
rows2=int(input("enter the number of rows for first matrix:"))
cols2=int(input("enter the number of cols for first matrix:"))
print("enter first matrix:")
B=[]
for i in range(rows2):
    row=list(map(int, input().split()))
    while len(row)!=cols2:
        print("invlaid input enter again")
        row=list(map(int, input().split()))
    B.append(row)
if rows1!=rows2 or cols1!=cols2:
    print("cant add matrix")
else:
    result = []
    for i in range(rows1):
        row=[]
        for j in range(cols1):
            row.append(A[i][j]+B[i][j])
        result.append(row)
    print("sum of the matric is :")
    for row in result:
        for element in row:
            print(element," ")
        print()