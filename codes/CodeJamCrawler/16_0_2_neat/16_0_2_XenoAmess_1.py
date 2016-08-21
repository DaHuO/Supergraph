def doit(str_line):
    i = len(str_line) - 1;
    ans = 0;
    while(1):
        if(str_line[i]=='-'):
            break;
        if(i==0):
            return 0;
        i-=1;
    
    i-=1;
    ans+=1;
    while(i>=0):
        if(str_line[i]!=str_line[i+1]):
            ans+=1;
        i-=1;  
    return ans;
        
        
        
                



file_in = open("in.txt", 'r+');
file_out = open("out.txt", 'w+');
T = int(file_in.readline());
t = 0;
while(1):
    lines = file_in.readlines(100000);
    if not lines:
        break;
    for line in lines:
        t += 1;
        file_out.write('Case #%d: %d\n' % (t, doit(line)));
    
file_in.close();
file_out.close();
        
    
