def rotate_string(s,goal):
    for i in range(len(s)):
        if(s[i:]+s[0:i]==goal):
            return True
        
s=input()
goal=input()

print(rotate_string(s,goal))