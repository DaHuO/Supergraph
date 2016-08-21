import sys
import math

def main(argv):
	inputfile = open(argv[1],'r')
	outputfile = open(argv[1].replace("in","out"),'w')

	testcase = int(inputfile.readline())

	if testcase > 1:
			print "Error. Wrong assumption"

	inputstr = inputfile.readline()
	N = int(inputstr.split(" ")[0])
	J = int(inputstr.split(" ")[1])

	print N
	print J

	outputfile.write("Case #1:\n")
	start = pow(2,N)/2+1
	for i in range(start, pow(2,N),2):
			if J == 0:
					return
			divisors = []
			div = find_div(i)
			prime = False
			#if prime, continue
			#else add to divisor
			if div == 1:
					#print "PRIME!: " + str(i)
					prime=True
					continue
			else:
				divisors.append(div)

			for j in range (3,11):
					base_num = find_base(i, j)
					#print str(i) + " " + str(j) + " " + str(base_num)
					div = find_div(base_num)
					#if prime, break
					#else add to divisor
					if div == 1:
					#		print "PRIME: " + str(base_num)
							prime=True
							break
					else:
							divisors.append(div)
			if not prime:
					J = J-1
					binary = convert_bin(i)
					outputfile.write(str(binary) + " " + str(" ".join(str(x) for x in divisors)) + "\n")

def convert_bin(num):
		num_copy = num
		binary = ""
		while num_copy >= 1:
				binary = str(num_copy%2) + binary
				num_copy = num_copy/2
		return binary

def find_base(num, base):
		binary = convert_bin(num)
		#print binary
		base_num = 0
		index = 0
		for c in reversed(binary):
			base_num = base_num + pow(base, index) * int(c)
			index = index + 1
		return base_num

def find_div(num):
		sqrt = math.sqrt(num)
		#dict = {False:1}
		for i in range(2, int(sqrt)+1):
				#print str(num) + "%" + str(i) + "=" + str(num%i)
				if num % i == 0 and i != num:
						return i
		return 1

	
if __name__ == "__main__":
		main(sys.argv)
