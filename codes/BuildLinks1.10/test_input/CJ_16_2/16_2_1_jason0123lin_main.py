def remove(m,c):
    n=m
    for (l,i) in enumerate(n):
        if i==c:
            n[l]=0
            break
    return n

def count(m):
    #print(m)
    sum=0
    z=[False]*10
    c=[0]*10
    for (l,i) in enumerate(m):
        sum+=i
        if i==26:
            z[0]=True
            c[0]+=1
            m[l]=0
        elif i==23:
            z[2]=True
            c[2]+=1
            m[l]=0
        elif i==21:
            z[4]=True
            c[4]+=1
            m[l]=0
        elif i==24:
            z[6]=True
            c[6]+=1
            m[l]=0
        elif i==7:
            z[8]=True
            c[8]+=1
            m[l]=0
    sum=sum-c[0]*64-c[2]*58-c[4]*60-c[6]*52-c[8]*49
    for j in range(c[0]):
        m=remove(m,5)
        m=remove(m,18)
        m=remove(m,15)
    for j in range(c[2]):
        m=remove(m,20)
        m=remove(m,15)
    for j in range(c[4]):
        m=remove(m,6)
        m=remove(m,18)
        m=remove(m,15)
    for j in range(c[6]):
        m=remove(m,19)
        m=remove(m,9)
    for j in range(c[8]):
        m=remove(m,5)
        m=remove(m,9)
        m=remove(m,8)
        m=remove(m,20)                                
    #print(sum,z,c,m)
    if sum==0: return c

    for (l,i) in enumerate(m):
        if i==15:
            z[1]=True
            c[1]+=1
        elif i==20:
            z[3]=True
            c[3]+=1
        elif i==6:
            z[5]=True
            c[5]+=1
        elif i==19:
            z[7]=True
            c[7]+=1
    sum=sum-c[1]*34-c[3]*56-c[5]*42-c[7]*65
    #print(sum,z,c,m)

    if sum==0: return c
    c[9]=sum//42
    #return sum
    return c

if __name__ == "__main__":
	tcases = input()

	#print("%s" % (testcases))
	for caseNr in range(1, int(tcases)+1):
		#n = int(input())
		m = [(ord(v) - ord('A')+1) for v in input()]
		s=count(m)
		print("Case #%i: " % (caseNr), end="")
		for (l,i) in enumerate(s):
			for j in range(i):
				print(l,end="")

		#[print(p, end="") for p in s]
		print("")
