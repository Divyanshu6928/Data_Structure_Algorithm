def isUnique(s):
    flag=True
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if(s[i] == s[j]):
                flag = False
            
    
    if(not(flag)):
        return "String is not Unique"
    else:
        return "String is Unique"

s=input()
print(isUnique(s))