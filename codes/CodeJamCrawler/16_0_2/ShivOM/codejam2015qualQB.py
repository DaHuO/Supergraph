import sys
inFile = sys.argv[1]
outFile = sys.argv[2]
pline=[]
c=0
cc=1
with open(inFile,'r') as ii:
        lines = ii.readlines()
        print lines
        a=int(lines[0])
        #print a
        #ind=0
        #t=int(lines[ind])
        ind=1
        while(a>0):
                #print t,
                c=0
                ip=lines[ind]
                ind+=1
                #print ip
                l=len(ip)-1
                #print l
                while True:
                        i=0
                        if  ip[i]=='-':
                                while(ip[i]=='-' and i<l):
                                        i+=1
                                        #print i
                                if(i==l):
                                        c+=1
                                        #print c,
                                        break
                                else:
                                        for k in range(i):
                                                ip=ip[:k]+'+'+ip[k+1:]
                                        c+=1
                        elif ip[i]=='+':
                                while(ip[i]=='+' and i<l):
                                        i+=1
                                if(i==l):
                                        
                                        break
                                else:
                                        for k in range(i):
                                                ip=ip[:k]+'-'+ip[k+1:]
                                        c+=1
                        
                stt='Case #'+str(cc)+': '+str(c)
                print stt
                cc+=1
                pline+=[stt]
                a-=1
                
with open(outFile,'w') as o:
    for lin in pline:
        o.write("%s\n" % (lin))

#print pline

