out=[]

def histogram(s):
    for c in s:
        hst[c] += 1
    return 0
pan=''
fp = open('A-large.in', 'r+')
prog_list = fp.readlines()
t=prog_list.pop(0)

j=0
for line in prog_list:
    hst = {'E':0,'F':0,'G':0,'H':0,'I':0,'N':0,'O':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Z':0}
    ans=''
    j=j+1
    count_num=[0,0,0,0,0,0,0,0,0,0]
    pan=line[:-1]
    histogram(pan)
    count_num[0]=hst['Z']
    count_num[2]=hst['W']
    count_num[4]=hst['U']
    count_num[6]=hst['X']
    count_num[8]=hst['G']
    count_num[3]=hst['H']-count_num[8]
    count_num[5]=hst['F']-count_num[4]
    count_num[7]=hst['V']-count_num[5]
    count_num[9]=hst['I']-count_num[6]-count_num[8]-count_num[5]
    count_num[1]=hst['O']-count_num[2]-count_num[4]-count_num[0]
    for i in xrange(0,10):
        len_ans=len(ans)
        ans=ans.ljust(len_ans+count_num[i],str(i))

    outstr="Case #" + str(j) + ": " + ans + "\n"
    out.append(outstr)
fp.close()
fpo = open('ophere_large.out', 'w+')
for line in out:
    fpo.write(line)
fpo.close()
  
