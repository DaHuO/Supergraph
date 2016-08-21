import time
def is_in(k,digit):
    flag=0
    for i in digit:
        if(k==i):
            flag=1
    return flag

with open('A-large.in','r') as f:
    read = [int(x) for x in next(f).split()] # read first line
    for line in f: # read rest of lines
        value=([int(x) for x in line.split()])
        #print value
        read.append(value[0])
    #array = [[int(x) for x in line.split()] for line in f]
#read=raw_input()
#print read
i=0
k=0
digit=[]
numbers_in_digit=[]
last_len=0
last_digit_seen=0
no=1
for case in read:
    if(no==1):
        no=no+1
        continue
    i=1
    k=0
    digit=[]
    numbers_in_digit=[]
    last_len=0
    last_digit_seen=0
    #print "case={0}".format(case)
    #print "read[]={0}".format(read[case])
    while(len(digit)!=10):
        if(case==0):
            last_digit_seen="INSOMNIA"
            #print "Case #{0} :Insomia".format(no)
            break
        k=long(case)*i
        last_digit_seen=k
        #print "K={0}".format(k)
        while(k/10!=0):
            numbers_in_digit.append(k%10)
            if(is_in(k%10,digit)==0):
                digit.append(k%10)
                #last_len=len(digit)
            k=k/10
        if(is_in(k,digit)==0):
            digit.append(k)
        #print digit
        i=i+1
    #print digit
    print "Case #{}: {}".format(no-1,last_digit_seen)
    no=no+1
    
        
    
    
