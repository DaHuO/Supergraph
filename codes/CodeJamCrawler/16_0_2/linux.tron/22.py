with open('B-large.in','r') as f:
    read = [str(x) for x in next(f).split()] # read first line
    case=read
    read=[]
    for line in f: # read rest of lines
        value=([str(x) for x in line.split()])
        #print value
        read.append(value[0])
string=[]
#print read
for string_1 in read:
    pos=0
    string_1=list(string_1)
    for i in string_1:
        if(i=='-'):
            string_1[pos]=0
        if(i=='+'):
            string_1[pos]=1
        pos=pos+1
    string.append(string_1)

#print string
def mask(value):
    count=0
    for i in value:
        count=count+1
    return count

case=1
for values in string:

    count=0
    group=[]
    flip=0
    flag=0
    j=0
    times=1

    #print "values={0}".format(values)
    #i=int(values)
    #print "i={0}".format(i)
    #print "j={0}".format(j)
    #print "count={0}".format(count)
    #print "flag={0}".format(flag)
    #print isinstance(i,int)
    for i in values:
        if((i==1 and j==0)):
            #print "01"
            if(count>0):
                if(flag==1):
                    flip=flip+2
                else:
                    flip=flip+1
                #print flip
                #group.append(0)
                #group.append(1)
            count=0
            #print "count={0}".format(count)
            j=i
            times=times+1
            continue
        if(i==0 and j==0):
            count=count+1
            #print "count={0}".format(count)
            #print "00"
            #print count
            #group.append(i)
            j=i
            times=times+1
            continue
        if(i==0 and j==1):
            count=count+1
            #print "count={0}".format(count)
            #print "10"
            flag=1
            #print "flag={0}",format(flag)
            #sub.append(i)
            j=i
            times=times+1
            continue
        if(i==1 and j==1):
            #group.append(1)
            #print "11"
            times=times+1    
            continue
    if(count>0):
        if(flag==1):
            flip=flip+2
        else:
            flip=flip+1
        count=0
    #print "flip={0}".format(flip)
    print "Case #{}: {}".format(case,flip)
    case=case+1
##        if(i==1):
##            flip=mask(group)
##            string[pos-1]=1    
##            string=string
##            flip=1
##        else:
##            if(flag==1):
##                flip=flip+1
##                flag=0
##            if(i==0 and j==1):
##                flag=1
##            group.append(i)
##                
  #  print flip

