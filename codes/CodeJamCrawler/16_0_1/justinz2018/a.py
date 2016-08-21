import sys

sys.stdin = open("A-large.in", "r")
sys.stdout = open("a-l.out", "w")
n = int(input())
for i in range(n):
	r = int(input())
	print("Case #{}: ".format(i+1), end="")
	if r == 0:
		print("INSOMNIA")
		continue
	a = [0]*10
	c2 = 1
	while True:
		t = str(r*c2)
		c2 += 1
		for c in t:
			a[ord(c)-ord('0')] = 1
		if sum(a) == 10:
			break
	print((c2-1)*r)
