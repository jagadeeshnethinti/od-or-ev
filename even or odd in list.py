n=int(input())
a=[]
b=[]
for i in range(n):
    r=int(input())
    if r%2==0:
        a.append(r)
    else:
        b.append(r)
print(a,b)