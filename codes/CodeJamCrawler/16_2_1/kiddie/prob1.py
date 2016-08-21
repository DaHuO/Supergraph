import numpy as np
n = input()
mydict = {'0':'ZERO', '1':'ONE','2':'TWO','3':'THREE','4':'FOUR','5':'FIVE','6':'SIX','7':'SEVEN','8':'EIGHT','9':'NINE'}
for j in xrange(n):
    s = raw_input()
    #print s
    s = sorted(s)
    for i in xrange(0,999999):
        mys = str(i)
        for k in mydict.keys():
            mys = mys.replace(k,mydict[k])

        mys = sorted(mys)
        if(mys == s):
            #print mys
            #print s
            no = str(i)
            naa = []
            for k in xrange(len(no)):
                naa.append(int(no[k]))
            sorte = np.sort(naa)
            a = ''
            for l in sorte:
                a = a+ str(l)
            print 'Case #%d: %s'%(j+1,a)
            break

            
    for mys in ['00','000','0000','00000']:
        no = mys
        for k in mydict.keys():
            mys = mys.replace(k,mydict[k])


        mys = sorted(mys)
        if(mys == s):
            #print mys
            #print s
            
            naa = []
            for k in xrange(len(no)):
                naa.append(int(no[k]))
            sorte = np.sort(naa)
            a = ''
            for l in sorte:
                a = a+ str(l)
            print 'Case #%d: %s'%(j+1,a)
            break
