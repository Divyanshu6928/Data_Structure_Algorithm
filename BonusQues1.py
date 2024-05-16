n=input()
l,r =map(int,input().split())
if(n[l:r]==n[r:l]):
    print("True")
else:
    print("False")