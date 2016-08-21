import sys

count =0
arr=list()
num=long(raw_input())
for i in range(0,num):
    ip=long(raw_input())
    arr.append(ip)

flag=0
count=1
arr2=set()
hell=1
for x in arr:
    x3=x
    x4=x3
    while flag!=1 and count!=100:
        while x3!=0:
            x2=x3%10
	    x3=long(x3/10)
	    arr2.add(x2)
        if len(arr2) is not 10:
	    count=count+1
	    x3=x*count
	    x4=x3
        else:
	    flag=1

    if count==100:
        print "Case #"+str(hell)+ ": INSOMNIA"
    elif flag==1:
	print "Case #"+str(hell)+": "+ str(x4)
    flag=0
    count=1
    arr2.clear()
    hell=hell+1
