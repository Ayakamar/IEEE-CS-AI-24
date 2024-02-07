A = list(map(int,input().split()))
for i in range(len(A)):
    if A[i]== -1:
        A.remove(A[i])
        print(max(A),min(A))
