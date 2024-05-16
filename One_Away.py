def OneAway(s1,s2):
    flag=True
    c=0
    if(len(s2)==len(s1)-1):
        flag=True
    if(len(s2)==len(s1)+1):
        flag=True
    if(len(s1)==len(s2)):
        
        for i in range(len(s1)):
            if(s1[i]==s2[i]):
                c+=1
        if(c==1):
            flag=True
        else:
            flag=False
        
    return flag

s1=input()
s2=input()
print(OneAway(s1,s2))