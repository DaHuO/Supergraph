import math

base_exp = dict()

def get_next_num(cur_num):
	carry = 1
	new_num = cur_num[-1]
	for i in xrange(len(cur_num)-2, -1, -1):
		n = int(cur_num[i])
		s = n+carry
		carry = int(s/2.0)
		s = s%2
		#print n,s,carry
		new_num += str(s)
			
	if carry==1:
		new_num += '1'
	
	new_num = new_num[::-1]
	return new_num

def is_jamcoin(num):
	if num[0]=='0' or num[-1]=='0':
		return False
	
	#Finiding non_trivial divisors of the number
	#Will only get if the number is not prime
	n_div_arr = []
	for b in xrange(2,11):
		N = conv_num(b, num)
		if N%2==0:
			n_div_arr.append(2)
			continue
			
		#print b,N
		lim = int(math.sqrt(float(N)))+1
		n_div = -1
		d = 3
		while d<lim:
			if N%d==0:
				n_div = d
				break
			d+=2
			
		if n_div==-1:
			return False
		n_div_arr.append(n_div)
		
	return n_div_arr
	
def conv_num(base_val, num):
	if base_val==10:
		return int(num)
		
	act_num = 0
	base_ls = base_exp[base_val]
	pos = 0	
	for i in range(len(num)-1,-1,-1):
		if num[i]=='1':
			act_num += base_ls[pos]
		pos += 1
	
	return act_num
	
if __name__ == "__main__":
	raw_input()
	for i in range(2,10):
		base_exp[i] = []
		for j in xrange(0,32):
			base_exp[i].append(i**j)
	
	N,J = [int(x) for x in raw_input().split()]
	
	num_found = 0
	num = "1"
	for i in range(1,N-1):
		num += '0'
	num += '1'
	
	print "Case #1:"
	while num_found<J and len(num)==N:
		#print "Cur Num:",num
		div_arr = is_jamcoin(num)
		if div_arr!=False:
			op_str = num
			for div in div_arr:
				op_str += ' ' + str(div)
			print op_str
			num_found += 1
			
		num = get_next_num(num)