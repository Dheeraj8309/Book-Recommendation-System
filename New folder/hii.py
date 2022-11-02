X=int(input())
K=int(input())
N=int(input())
A=[]
B=[]
for i in range(N):
    A.append(int(input()))
for i in range(N):
    B.append(int(input()))
for i in range(N):
    for j in range(0, N-i-1):
        if A[j] > A[j+1] :
            A[j], A[j+1] = A[j+1], A[j]
            B[j], B[j+1] = B[j+1], B[j]
sliceindex=[]
new_A=[]
new_B=[]
for i in range(N):
    if(A[i]<=X and B[i]>K):
        new_A.append(A[i])
        new_B.append(B[i])
A=new_A
B=new_B
current=[]
i=0
s=0
while(i<len(A)):
    s+=A[i]
    current.append(i)
    if(s>X):
        print(current.pop(-1))
        sliceindex.append(current)
        current=[]
        s=0
    else:
        i=i+1
sliceindex.append(current)
ans=0
for i in sliceindex:
    sum1=0
    for j in i:
        sum1+=B[j]
    ans+=sum1-K
print(ans)
        


    




