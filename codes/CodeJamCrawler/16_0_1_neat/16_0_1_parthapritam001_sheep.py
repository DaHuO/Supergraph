
def writeoutput(out,num):
    f=open("sheepout.txt","a")
    f.write("case #"+str(num)+": "+out+"\n")
    f.close()

import sets
list=[]
f=open("sheepout.txt","w")
f.close()
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in range(0, t):
    n = int(raw_input())  # read a list of integers, 2 in this case
    list.append(n)
#print list
#input collected now need to process
output=[]
o=set()
num=1
for item in list:
    i=1
    o.clear()
    while(True):
        it = i * item
        if it==0:
            print "case #"+str(num)+": "+"INSOMNIA"
            #writeoutput("INSOMNIA",num)
            num+=1
            break
        itemData=str(it)
        for j in itemData:
            o.add(j)
        if len(o)==10:
            print "case #"+str(num)+": "+str(it)
            #writeoutput(str(it),num)
            num+=1
            break
        else:
            i+=1
            continue


