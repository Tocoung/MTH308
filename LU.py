# A=[[1,2,1,3],[2,4,1,5],[3,2,1,4],[4,1,1,3]]
# L=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# U=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
A=[[2,0,1],[4,3,2],[6,0,5]]
L=[[0,0,0],[0,0,0],[0,0,0]]
U=[[0,0,0],[0,0,0],[0,0,0]]
k=0
n=3
while(k<n):
    # j=k+1
    # p=k
    # while(j<n):
    #     if(A[j][k]>A[k][k]):
    #         p=j
    #     j=j+1
    # temp=A[p]
    # A[p]=A[k]
    # A[k]=temp
    L[k][k]=1
    t=0
    p=0
    while(p<k):
        t=t+L[k][p]*U[p][k]
        p=p+1
    U[k][k]=A[k][k]-t
    i=k+1
    while(i<n):
        t=0
        p=0
        while(p<k):
            t=t+L[i][p]*U[p][k]
            p=p+1
        L[i][k]=(A[i][k]-t)/U[k][k]
        i=i+1
    j=k+1
    while(j<n):
        t=0
        p=0
        while(p<k):
            t=t+L[k][p]*U[p][j]
            p=p+1
        U[k][j]=A[k][j]-t
        j=j+1
    k=k+1
print(L)
print(U)