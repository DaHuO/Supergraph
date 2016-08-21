from math import sqrt

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))

def is_base_ok(binaryString, base):
	num = 0
	p = len(binaryString)-1 
	for i in binaryString:
		num+=(pow(base,p)*int(i))
		p-=1
	return (is_prime(num), num)

def any_divisor(num):
	sz = int(sqrt(num))+4
	for i in range(2,sz):
		if num%i == 0 and i!=1 and num/i!=1:
			return num/i

t = int(raw_input())
m = map(int, raw_input().split(" "))
n = m[0]
j = m[1]

start = 0
end = 1<<n-3
for i in range(1,n-2):
	end|=(1<<(n-3-i))


for i in range(1,t+1):
	str1 = "Case #"+str(i)+": "
	print str1
	cnt_ans = 0
	for x in range(start, end+1):

		tmpStr = "{0:b}".format(x)
		tmpStr2 = (n-2-len(tmpStr))*"0"
		binaryString = "1" + tmpStr2 +tmpStr + "1"
		
		base_divs = []
		for base in range(2,11):
			tmp = is_base_ok(binaryString, base)
			if tmp[0] == False:
				base_divs.append(any_divisor(tmp[1]))
		if len(base_divs) == 9:
			cnt_ans+=1
			str2 = binaryString+" "
			for divisors in base_divs:
				str2+=str(divisors)
				str2+=" "
			print str2
			if cnt_ans == j:
				break

