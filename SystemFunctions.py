def jac(x1,x2,x3):
    # x11=2*x1+x2
    # x12=x1
    # x21=3*x2**2
    # x22=1+6*x1*x2
    # return [[x11,x12],[x21,x22]]
    x11=1
    x12=1
    x13=1
    x21=2*x1
    x22=2*x2
    x23=2*x3
    x31=3*x1**2
    x32=3*x2**2
    x33=3*x3**2
    return [[x11,x12,x13],[x21,x22,x23],[x31,x32,x33]]

def f(x,y,z):
    x1=x+y+z-0.3
    x2=x**2+y**2+z**2-0.03
    x3=x**3+y**3+z**3-0.003
    return [x1,x2,x3]

x=[0.15,0.05,0.2]
e=1
iter=1
while(iter<50):
    a=jac(x[0],x[1],x[2])
    b=f(x[0],x[1],x[2])
    print(iter,end="\t")
    print(x,end="\t")
    print(a,end="\t")
    print(b,end="\t")
    n=3
    i=0
    c=x
    while(i<n):
        j=i
        p=j
        while(j<n):
            if(abs(a[p][i])<abs(a[j][i])):
                p=j
            j=j+1
        j=0
        while(j<n):
            temp=a[p][j]
            a[p][j]=a[i][j]
            a[i][j]=temp
            j=j+1
        temp=b[p]
        b[p]=b[i]
        b[i]=temp
        j=i+1
        while(j<n):
            m=a[j][i]/a[i][i]
            k=i+1
            a[j][i]=0
            while(k<n):
                a[j][k]=a[j][k]-m*a[i][k]
                k=k+1
            b[j]=b[j]-m*b[i]
            j=j+1
        i=i+1
    i=n-1
    x=b
    while(i>=0):
        j=i+1
        while(j<n):
            x[i]=x[i]-x[j]*a[i][j]
            j=j+1
        x[i]=x[i]/a[i][i]
        i=i-1
    i=0
    while(i<n):
        x[i]=(-1)*x[i]
        i=i+1
    print(x,end="\t")
    i=0
    nu=0
    dn=0
    while(i<n):
        nu=nu+(x[i])**2
        dn=dn+(x[i]+c[i])**2
        i=i+1
    i=0
    while(i<n):
        x[i]=x[i]+c[i]
        i=i+1
    print(x,end="\t")
    e=nu/dn
    e=e**0.5
    print(e)
    iter=iter+1
