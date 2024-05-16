t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=0
    for j in range(len(a)):
        s+=a[j]
    c=0
    for j in range(len(a)):
        if(a[j]+k > s-a[j]):
            c+=1
    print(c)