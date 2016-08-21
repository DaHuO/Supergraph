def remove_endlines(orignal_data):
    new_data=""
    orignal_data=orignal_data.replace('\r','')
    orignal_data=orignal_data.replace('\n','')
    if orignal_data!="":
        new_data=orignal_data
    return new_data


testfile=open('A-large.in','r')
ndata=testfile.readlines()
for k in range(1,len(ndata)):
    fullList=['0','1','2','3','4','5','6','7','8','9']
    ndata[k]=remove_endlines(ndata[k])
    if ndata[k]=='0':
        print "Case #{}:".format(k),'INSOMNIA'
    else:
        Num=ndata[k]
        counter=1
        while len(fullList)!=0:
            for i in range(len(Num)):
                if Num[i] in fullList:
                    fullList.remove(Num[i])
                    if len(fullList)==0:
                        break
            if len(fullList)!=0:
                counter=counter+1
                Num=str(int(ndata[k])*(counter))
        print "Case #{}:".format(k),Num
testfile.close() 
