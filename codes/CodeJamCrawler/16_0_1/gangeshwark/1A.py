def count(n,a):
	i=1
	lst=[]
	list1=[0,1,2,3,4,5,6,7,8,9]
	while(True):
		n1=i*n
		t=n1
		while(t!=0):
			rem=t%10
			t=t/10
			if rem not in lst:
				lst.append(rem)
				lst.sort()
		if sublistExists(list1,lst):
			print "Case #%d: "%a + str(n1)
			break
		i+=1
		if (i==1000):
			print "Case #%d: "%a + "INSOMNIA"
			break



def sublistExists(list1, list2):
    return ''.join(map(str, list1)) in ''.join(map(str, list2))

if __name__ == '__main__':
	n=int(raw_input())
	for i in xrange(n):
		count(int(raw_input()),i+1)