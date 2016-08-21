f = open('A-large.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

def find_last_num(N):
	has_seen_digit = [0]*10
	num_of_seen_digits = 0
	curr_number = N
	while num_of_seen_digits < 10:
		n = curr_number
		length = len(str(n))
		for i in range(length):
			curr_digit = n % 10
			if has_seen_digit[curr_digit] == 0:
				has_seen_digit[curr_digit] = 1
				num_of_seen_digits += 1
			n /= 10
		curr_number += N
	return  curr_number - N



for t in xrange(T):
    N = int(f.readline().strip())
    if N == 0:
    	s = "Case #%d: INSOMNIA\n" % (t+1)
    else:
    	result = find_last_num(N)
    	s = "Case #%d: %s\n" % (t+1, result)
    print s
    o.write(s)