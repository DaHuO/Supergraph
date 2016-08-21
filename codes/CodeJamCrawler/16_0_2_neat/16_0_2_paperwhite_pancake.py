import sys

def flip(string, pos):
    count =0
    result=""
    for char in string:
	if count <= pos:
            if char is "+":
    	        result=result+"-"
	    elif char is "-":
	        result=result+"+"
            count=count+1
	else:
	    result=result+char
    return result

arr=list()
num=long(raw_input())
for i in range(0,num):
    ip=sys.stdin.readline().strip()
    arr.append(ip)

hell=1
for x in arr:
    flips=0
    if x is None:
	continue
    else:
        k = x.rfind("-")
	while k!=-1:
	    x=flip(x,k)
	    flips=flips+1
	    k=x.rfind("-")
        print "Case #"+str(hell)+": "+str(flips)
	hell=hell+1
