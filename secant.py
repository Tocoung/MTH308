def f(x):
    return 2*x**3-2.5*x-5

x1=1
x2=2
x=x2-f(x2)*(x2-x1)/(f(x2)-f(x1))
fx=f(x)
i=1
r=[]
r.append(("Iteration","x1","x2","x","f(x)"))
while(i<=5):
    r.append((i,x1,x2,x,fx))
    x1=x2
    x2=x
    x=x2-f(x2)*(x2-x1)/(f(x2)-f(x1))
    fx=f(x)
    i=i+1

with open("Prithviraj_Ghosh_secant_output.txt",'w') as file:
    i=0
    for row in r:
        if(i==0):
            file.write(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\n")
        else:
            file.write(f"{row[0]}\t{row[1]:.10f}\t{row[2]:.10f}\t{row[3]:.10f}\t{row[4]:.10f}\n")
        i=i+1