# t = int(raw_input())  # read a line with a single integer
# for i in xrange(1, t + 1):
#   n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
#   print "Case #{}: {} {}".format(i, n + m, n * m)

def countSheep(number):
	if(number==0):
		return "INSOMNIA"
	intList = []
	for i in str(number):
		x=int(i)
		if x not in intList:
			intList.append(x)
	flag=False;
	n=2;
	while(flag==False):
		newnumber=number*n
		newIntList= [int(i) for i in str(newnumber)]
		for x in newIntList:
			if x not in intList:
				intList.append(x)
		if len(intList)==10:
			return newnumber;
			flag=True
		n+=1


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = [int(s) for s in raw_input().split(" ")] 
  res = countSheep(n[0])
  print "Case #{}: {}".format(i, res)

