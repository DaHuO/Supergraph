import math
f = open('C-large.in','r')
out = open('output1.txt','w')
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    cnt = 3
    for i in prime:
    	if n%i == 0:
    		return False
    return True

def firstDiv(n):
	cnt = 2
	while(n%cnt != 0 and cnt!=n):
		cnt += 1
	if cnt != n:
		return cnt

def CoinJam(l,j):
	cnt = 0
	counter = 0
	while(cnt < j):
		num = "1"+bin(counter)[2:].zfill(l-2)+"1"
		prime = 0
		for i in range(2,11):
			if is_prime(int(num,i)):
				prime = 1
		if prime == 0:
			div = []
			for i in range(2,11):
				div.append(firstDiv(int(num,i)))
			if(len(div) == 9):
				cnt += 1
				out.write(str(num))
				for k in div:
					out.write(" "+str(k))
				out.write("\n")
		counter+=1

tests = int(f.readline())
for i in range(1,tests+1):
	l,j = f.readline().split(" ")
	out.write("Case #"+str(i)+":"+"\n")
	CoinJam(int(l),int(j))
