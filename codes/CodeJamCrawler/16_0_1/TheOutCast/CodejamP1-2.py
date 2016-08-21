import os
def cheep(x):
    
    s=['0','1','2','3','4','5','6','7','8','9']
    if(x==0):
        return "INSOMNIA"
    
    for i in range(1,100):
        xn=i*x
        for y in str(xn):
            try:
                c=s.index(y)
                s.pop(c)
            except ValueError:
                pass
            
        if(len(s)==0):
            return xn
fname="A-large.in"
output="Output-CodeJam-P1-2.txt"
if(os.path.isfile(output)):
    os.remove(output)
content = [content.rstrip('\n') for content in open(fname)]
for i in range(1,int(content[0])+1):
    with open(output, "a") as text_file:
        print("Case #"+str(i)+": "+str(cheep(int(content[i]))),file=text_file)
