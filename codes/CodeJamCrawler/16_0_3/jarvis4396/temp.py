import random,math
 
_mrpt_num_trials = 5 
 
def is_probable_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True 
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True 

text_file = open("output.txt", "w")
lines = [line.rstrip('\n') for line in open('input.txt')]
t = int(lines[0])
for k in range(1,t+1):
	text_file.write('Case #' + str(k) + ':\n')
	s = lines[k]
	s = s.split()
	n = int(s[0])
	p = int(s[1])

	c1 = 0
	c2 = 0

	while(c2 != p):

		s = '1'
		s1 = "{0:b}".format(c1)

		for i in range(0,n-2-len(s1)):
			s = s + '0'

		s = s + s1 + '1'

		a = []
		flag = 0

		for i in range(2,11):
			x = int(s,i)
			a.append(x)
			if(is_probable_prime(x)):
				flag = 1
				break

		if(flag == 0):
			text_file.write(s + ' ')
			for i in range(0,len(a)):
				if(a[i]%2 == 0):
					text_file.write('2 ')
				else:
					for j in range(3,int(math.sqrt(a[i]))+1,2):
						if(a[i]%j == 0):
							text_file.write(str(j) + ' ')
							break
			text_file.write('\n')
			c2 = c2 + 1
		c1 = c1 + 1
text_file.close()