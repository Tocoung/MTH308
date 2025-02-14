import random
j=0
while(j<5):
    i=0
    s=0
    n=2000000
    while(i<n):
        e=random.random()
        if(e>0.5):
            e=1-e
        while(1+e!=1):
            e=e/10
        s=s+e
        i=i+1
    print(s/n)
    j=j+1