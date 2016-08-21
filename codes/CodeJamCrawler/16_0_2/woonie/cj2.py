def largest_index(num, a):
	b = [i for i, j in enumerate(a) if j == num]
	if len(b) == 0:
		return -1
	else:
		return b[len(b) -1]
def check(a, flg, count):
	if flg:
		c = largest_index('+', a)
	else:
		c = largest_index('-', a)
	if c == -1:
		return count
	else:
		return check(a[:c+1], not flg, count+1)
def main():
	
	f = open('cj2.txt', 'r')
	l = int(f.readline())
	for i in range(l):
		count = 0
		out = "Case #" + str(i+1) + ": "
		t = f.readline()
		tt = list(t)
		res = check(tt, False, 0)
		print out + str(res)

main()