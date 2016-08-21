fh = open("dataset.txt")
num=int(fh.readline())
data = [int(x) for x in fh.read().split("\n")]
for i in range(num):
    freq=[0]*10
    temp=0
    print "Case #"+str(i+1)+":",
    if data[i]==0:
        print "INSOMNIA"
        continue
    while min(freq)==0:
        temp+=1
        n=temp*data[i]
        while n>0:
            freq[n%10]+=1
            n/=10    
        
        if max(freq)>1000:
            print "INSOMNIA"
            break
    if min(freq)>0:
        print temp*data[i];