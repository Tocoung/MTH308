def f(x):
    return 2*x**3-2.5*x-5
def df(x):
    return 6*x**2-2.5
x=2
fx=f(x)
dfx=df(x)
e=float('inf')
i=1
r=[]
r.append(("Iteration","x","x1","f(x)"))
while(i<5):
    xn=x-fx/dfx
    fx=f(xn)
    dfx=df(xn)
    r.append((i,x,xn,fx))
    e=abs(xn-x)*100/abs(x)
    x=xn
    i=i+1

with open("Prithviraj_Ghosh_A_2_output.txt",'w') as file:
    i=0
    for row in r:
        if(i==0):
            file.write(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\n")
        else:
            file.write(f"{row[0]}\t{row[1]:.10f}\t{row[2]:.10f}\t{row[3]:.10f}\n")
        i=i+1