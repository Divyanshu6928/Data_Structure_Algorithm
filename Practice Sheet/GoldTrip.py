# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    q=int(input())
    for j in range(q):
        qu=list(map(int,input().split()))
        for k in range(len(qu)):
            s=0
            s+=sum(a[qu[0]-1:qu[1]])
            print(s)
            break