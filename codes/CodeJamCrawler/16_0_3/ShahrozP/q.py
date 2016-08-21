import math

def string_to_num(binary,base):
 	l = len(binary)-1
 	num = 0
 	for x in binary:
 		num += int(x)*((base)**(l))
 		l -=1
 	return num

def num_to_string(num):
	binary = ""
	while num>0:
		if num%2==0:
			binary += "0"
		else:
			binary += "1"
		num = math.floor(num/2)
	return binary[::-1]

def insert_divisor(binary,base,divisor):
	num = string_to_num(binary,base)
	# print num
	if num%2==0:
		# print num
		divisor.append(2)
		return 1
	else:
		div = 3;
		while div <5000:
			if num%div==0:
				divisor.append(div)
				return 1
			else:
				div +=2
	# print "next"
	return 0


t = int(raw_input())
base = [2,3,4,5,6,7,8,9,10]
for i in range(1, t + 1):
	# n , j = [int(s) for s in raw_input().split(" ")]
	n = int(raw_input())
	j = int(raw_input())
	count =0
	print "Case #{}:".format(i)
  	lower = (2**(n-1))+1
  	upper = (2**(n))
  	# print lower
  	# print upper
  	for x in range(lower,upper):
  		# print x, "yes"
  		if x%2==1:
  			divisor = []
  			binary_string = num_to_string(x)
  			# print binary_string
  			for b in base:
  				if (insert_divisor(binary_string,b, divisor)==0):
  					break;
  			if (len(divisor)==9):
  				count+=1;  	
  				print binary_string,
  				for d in divisor:
  					print d,
  				print
  		if count==j:
  			break;

