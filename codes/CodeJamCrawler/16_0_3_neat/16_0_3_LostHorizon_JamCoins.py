import math

def get_factor(n):
    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return False

def gen(n):
     for i in xrange(1, 2**n-1):
         yield '{:0{n}b}'.format(i, n=n)

def convert_to_base(x,b):
	num = 0
	for j in range(len(x)):
		if x[len(x)-j-1] == "1":
			num += pow(b,j)
	return num

def bf_generatecoins():
	g = open("C-small-out.txt", "w")
	g.write("Case #1:\n")
	succ = 0 
	for x in list(gen(14)):
		y = "1" + x + "1"
		curr_answer = y 
		for j in range(2,11):
			# print y, j
			curr_number = convert_to_base(y,j)
			
			X = get_factor(curr_number)
			
			if X:
				curr_answer += " " + str(X)
			else:
				break
			if j == 10:
				g.write(curr_answer + "\n")
				print curr_answer, succ
				succ = succ + 1

		if succ == 50:
			break


print convert_to_base("1111111001101111",3)
bf_generatecoins()