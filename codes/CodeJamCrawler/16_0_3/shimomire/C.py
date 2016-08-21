import sys

T = int(input())
N,J = map(int,input().split())

print("Case","#1:")
for bit in range(1 << (N-2)):
	vs = [0]*11
	v = (1 << (N-1)) + (bit<<1) + 1
	for base in range(2,10+1):
		vt = v;val = 0;d = 0
		while(vt != 0) :
			val += (vt%2) * (base ** d)
			vt //= 2
			d += 1
		vs[base] = val;
	# cerr << vs << endl;
	res = [-1]*11
	ok = True
	for base in range(2,10+1):
		for p in range(2,200000):
			if(p*p > vs[base]):
				break
			if(vs[base] % p == 0):
				res[base] = p
				break
		if(res[base] == -1):
			ok = False; break
	if(not ok) :
		continue

	print(vs[10],end="")
	for base in range(2,10+1):
		print("",res[base],end="")
	print()
	J-= 1
	if J==0 :
		break
