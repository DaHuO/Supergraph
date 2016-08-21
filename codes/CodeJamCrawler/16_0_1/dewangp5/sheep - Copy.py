out=[]
fp = open('A-large.in', 'r+')
prog_list = fp.readlines()
t=prog_list.pop(0)
i=0
num=''
for line in prog_list:
    i=i+1
    num=''
    line=line[:-1]
    list1=['0','1','2','3','4','5','6','7','8','9']
    num=line.rstrip('0')
    #print num
    nzero=len(line)-len(num)
    if(nzero>0):
        list1.remove('0')
    if len(num)==0:
        outstr="Case #" + str(i) + ": INSOMNIA\n"
        #print outstr
    else:
        dig=int(num)
        n=1
        while(len(list1)>0):
            digit=n*dig
            dig_str=str(digit)
            dig_l=list(dig_str)
            #print dig_l
            for item in dig_l:
                #print "::"+item
                if item in list1:
                    list1.remove(item)
            n=n+1
            #print list1
        ans=str(digit)
        len_ans=len(ans)
        ans=ans.ljust(len_ans+nzero,'0')
            
        outstr="Case #" + str(i) + ": " + ans + "\n"
    out.append(outstr)
    #print out
fp.close()
fpo = open('sheep_try_large.out', 'w+')
for line in out:
    fpo.write(line)
fpo.close()
