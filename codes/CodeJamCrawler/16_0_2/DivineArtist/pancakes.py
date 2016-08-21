'''
    flipping pancakes
'''
inpt = open("dataset.txt")
outpt= open("results.txt","w")
num=int(inpt.readline())
for i in range(num):
    data=inpt.readline().strip()
    num=sum([1 for j in range(1,len(data)) if data[j]!=data[j-1]])
    if ((num%2==0 and data[0]=="-") or (num%2==1 and data[0]=="+")):
        num+=1
    #print data, num, len(data)
    print "Case #"+str(i+1)+": "+str(num)