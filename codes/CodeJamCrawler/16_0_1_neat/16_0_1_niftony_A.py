file=open("A-large.in","r")
file_out=open("A-small.out","wr")

case_n=file.readline()

for x in xrange(int(case_n)):
    case_id=x+1
    case_v=int(file.readline())
    buffer=[]
    tmp=case_v
    if tmp==0:
        file_out.writelines("Case #"+str(case_id)+": "+"INSOMNIA\n")
    else:
        count=1
        while len(buffer)!=10:
            for x in str(tmp):
                if not x in buffer:
                    buffer.append(x)
            count+=1
            tmp=count*case_v
        file_out.writelines("Case #"+str(case_id)+": "+str(tmp-case_v)+"\n")

