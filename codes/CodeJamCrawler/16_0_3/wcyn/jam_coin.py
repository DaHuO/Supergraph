import itertools
import math

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        # print '\t',f
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True    

def has_prime(list_num):
    for i in list_num:
        if is_prime(i):
            return True
    return False

def get_first_non_trivial_divisor(num):
	for i in range(2,int(math.sqrt(num))+1):
		if num % i == 0:
			return i

def jam_coin(filename_in, filename_out):
	with open(filename_in, "r") as input_f:
		test_cases = int(input_f.readline());
		for x in range(test_cases):
			N,J = input_f.readline().replace("\n","").split()
			N = int(N)
			J = int(J)
			# print "N:%s, J:%s"%(N,J)
			# N = 4
			prods = ["".join(seq) for seq in itertools.product("01", repeat=N-2)]
			# print "Prods: ",prods
			jamcoin_start = "1" + prods[0] + "1"
			jamcoins = 0
			loop = 1
			divisor_list = []
			jamcoins_list = []
			while jamcoins < J:
				base_nums = []
				for a in range(2, 10):
					base_nums.append(int(jamcoin_start,a))
				base_nums.append(int(jamcoin_start)) # avoid calculating for base 10
				# print "base nums: ", base_nums
				if not has_prime(base_nums):
					jamcoins += 1
					jamcoins_list.append(jamcoin_start)
					# print "Yay jamcoin! ", jamcoin_start
					non_trivials = []
					for c in base_nums:
						non_trivials.append(get_first_non_trivial_divisor(c))
					divisor_list.append(non_trivials)
					# print "non_trivials: ", non_trivials
				if loop >= len(prods):
					print "not enough jamcoins :("
					break
				else:
					jamcoin_start = "1" + prods[loop] + "1"
				loop += 1
				# print "\nNew jamcoin: %s\n"%(jamcoin_start)

			mode = "a"			
			with open(filename_out,mode) as output_f:
				output_f.write("Case #%d:\n" %(x+1))
				for a in range(len(jamcoins_list)):
					output_f.write("%s"%(jamcoins_list[a]))
					for b in divisor_list[a]:
						output_f.write(" %s" %(b))
					output_f.write("\n")
jam_coin("C-small-attempt1.in", "C-small-attempt1.out")
 