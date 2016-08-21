import re
i=0
out=[]
pan=''
fp = open('B-large.in', 'r+')
prog_list = fp.readlines()
t=prog_list.pop(0)
i=1
for line in prog_list:
    pan=line[:-1]
    pan=pan.replace('+','p')
    pan=pan.replace('-','m')
    #print pan
    repeat = re.compile(r'(?P<start>[a-z])(?P=start)*-?')
    count=0
    for match in repeat.finditer(pan):
        count=count+1
        if(match.group()[0]=='p'):
            last=1
        else:
            last=0
    if(last==0):
        ans=count
    else:
        ans=count-1
    outstr="Case #" + str(i) + ": " + str(ans) + "\n"
    #print outstr
    i=i+1
    out.append(outstr)
    #print out
fp.close()
fpo = open('finale_large.out', 'w+')
for line in out:
    fpo.write(line)
fpo.close()
  




  
  
  
