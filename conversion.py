a=int(input())
b=int(input())
n=input()
l=len(n)
d=0
i=0
j=0
for c in n:
    if(ord(c)>=65 and ord(c)<=70):
        j=10+(ord(c)-65)
    else:
        j=int(c)
    d=d+j*a**(l-i-1)
    i=i+1
s=""
while(d!=0):
    f=d%b
    if(f>10):
        s=str(chr(ord('A')+(f-10)))+s
    else:
        s=str(f)+s
    d=d//b
print(s)