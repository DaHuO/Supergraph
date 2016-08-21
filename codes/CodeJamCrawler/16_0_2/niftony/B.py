file=open("B-large.in","r")
file_out=open("B.out","wr")

# always set the last nonone number to 1
case_n=file.readline()
for x in xrange(int(case_n)):

    case_id=x+1
    case_v=file.readline().strip()
    # from the back to front
    end=len(case_v)-1
    count=0
    flag="+"
    for index in xrange(end,-1,-1):
        if case_v[index]!=flag:
            if flag=='+':
                flag='-'
            else:
                flag='+'
            count+=1

    file_out.writelines("Case #"+str(case_id)+": "+str(count)+"\n")
