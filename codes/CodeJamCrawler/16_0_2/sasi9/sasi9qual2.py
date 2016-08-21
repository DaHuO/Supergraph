n=int(raw_input())
s=[];
g=0;
count=0;
def flipn():
    for j in range(len(s)):
        if(s[j]=='-'):
            s[j]='+';
        elif(s[j]=='+'):
            return;
def flipp():
    for j in range(len(s)):
        if(s[j]=='+'):
            s[j]='-';
        elif(s[j]=='-'):
            return;
        
def flip():
    if(s[0]=='-'):
        flipn();
    elif(s[0]=='+'):
        flipp();
        
for i in range(n):
    s=list(raw_input());
    while(g<30):
        if(set(s)=={'+'}):
            break;
        else:
            flip();
            count=count+1;
        g=g+1;
    print "Case #"+str(i+1)+": "+str(count);
    count=0;
    g=0;
