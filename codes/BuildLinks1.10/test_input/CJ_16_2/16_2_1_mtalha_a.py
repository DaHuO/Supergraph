import sys
if __name__ == '__main__':
	x=int(sys.stdin.readline())
	for i in range(x):
		x=str(sys.stdin.readline())
		zero=x.count('Z')
		two=x.count('W')
		eight=x.count('G')
		three=x.count('H')-eight
		six=x.count('X')
		four=x.count('U')
		five=x.count('F')-four
		seven=x.count('V')-five
		nine=x.count('I')-six-eight-five
		one=x.count('O')-zero-two-four
		ans=""
		for j in range(zero):
			ans=ans+"0"
		for j in range(one):
			ans=ans+"1"
		for j in range(two):
			ans=ans+"2"
		for j in range(three):
			ans=ans+"3"	
		for j in range(four):
			ans=ans+"4"
		for j in range(five):
			ans=ans+"5"
		for j in range(six):
			ans=ans+"6"
		for j in range(seven):
			ans=ans+"7"
		for j in range(eight):
			ans=ans +"8"
		for j in range(nine):
			ans=ans+"9"	
		print "Case #"+str(i+1)+": "+ans	