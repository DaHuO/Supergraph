import fileinput
cases = int(fileinput.input())
for i in range(1,cases+1):
    line = fileinput.input()
    length=len(line)
    flips=0
    for j in range(len(line)-1):
        if(line[j]!=line[j+1]):
            flips+=1          
    if(((line[0]=='+')&(line[length-1]=='-'))|((line[0]=='-')&(line[length-1]=='-'))):
        flips+=1
   
    print("Case #%i: %i" %(i,flips))
