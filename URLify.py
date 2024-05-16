def URLify(s,l):
    news=""
    for i in range(0,l):
        if(s[i]==' '):
            news+="%20"
        else:
            news+=s[i]
        
    return news

s=input()
l=int(input())
print(URLify(s,l))