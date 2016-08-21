import sys
inFile = sys.argv[1]
outFile = sys.argv[2]
pline=[]
with open(inFile,'r') as i:
        lines = i.readlines()
        a=int(lines[0])
        #print lines[0][0:-2]
        #print('\n'.join('{}: {}'.format(*k) for k in enumerate(lines)))
        t=1
        while t<=a:
                gain=''
                m=1
                b=int(lines[t])
                #print b,
                if b==0:
                        line='Case #'+str(t)+': INSOMNIA'
                        t+=1
                        pline+=[line]
                        continue
                count=0
                stt=b
                while count<10:
                        b=str(int(stt)*m)
                        #print b,count
                        m+=1
                        for i in b:
                                if i in gain:
                                        continue
                                else:
                                        gain+=i
                                        count+=1
                                        
                line='Case #'+str(t)+': '+str(b)
                pline+=[line]
                t+=1
with open(outFile,'w') as o:
    for lin in pline:
        o.write("%s\n" % (lin))

#print pline

