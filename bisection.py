def f(x):
    return x**3-0.165*x**2+0.0003993

xl=0
xh=0.11
xm=(xl+xh)/2
e=float('inf')
func=f(xm)
i=0
row=[]
row.append(("Iteration","xl","xu","xm","absolute relative approximate error","f(xm)"))
while(e>0.1):
    row.append((i+1,xl,xh,xm,e,func))
    c=xm
    if(func*f(xl)<0):
        xl=xl
        xh=xm
    else:
        xl=xm
        xh=xh
    xm=(xl+xh)/2
    func=f(xm)
    e=abs(xm-c)*100/abs(xm)
    i=i+1

head=["Iteration","xl","xu","xm","absolute relative approximate error","f(xm)"]
with open("Prithviraj_Ghosh_A_1_output.txt","w") as file:
    #csvfile.write(("Iteration\txl\txu\txm\tabsolute relative approximate error\tf(xm)\n"))
    i=0
    for r in row:
        #file.write(f"{r[0]}\t{r[1]:.6f}\t{r[2]:.6f}\t{r[3]:.6f}\t{r[4]:.6f}\t{r[5]:.6f}\n")
        if(i==0):
            file.write(f"{r[0]}\t{r[1]}\t\t\t{r[2]}\t\t\t{r[3]}\t\t\t{r[4]}\t\t{r[5]}\n")
        else:
            file.write(f"{r[0]}\t\t\t{r[1]:.6f}\t{r[2]:.6f}\t{r[3]:.6f}\t{r[4]:4f}\t\t\t\t\t\t\t\t{r[5]:.8f}\n")
        i=i+1
    # csvwriter=csv.writer(csvfile)
    # csvwriter.writerow(head)
    # csvwriter.writerows(row)

# from tabulate import tabulate
# def f(x):
#     return x**3 - 0.165 * x**2 + 0.0003993
# xl = 0
# xh = 0.11
# xm = (xl + xh) / 2
# e = float('inf')
# func = f(xm)
# i = 0
# rows = []
# while e > 0.1:
#     rows.append([i+1, f"{xl:.6f}", f"{xh:.6f}", f"{xm:.6f}", f"{e:.4f}", f"{func:.8f}"])
#     c = xm
#     if func * f(xl) < 0:
#         xh = xm
#     else:
#         xl = xm
#     xm = (xl + xh) / 2
#     func = f(xm)
#     e = abs(xm - c) * 100 / abs(xm)
#     i += 1
# headers = ["Iteration", "xl", "xu", "xm", "Absolute Relative Approximate Error (%)", "f(xm)"]
# table = tabulate(rows, headers=headers, tablefmt="grid")
# with open("Prithviraj_Ghosh_A_1_output.txt", "w") as file:
#     file.write(table)
