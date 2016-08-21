import sys

lp = [ [] for i in range(11) ]

def ok(x):
	s = str( bin(x) )[2:]
	for b in range(2,11):
		p = 1
		cur = 0
		j = 0
		while j < 32:
			if ( x & (1<<j) ) > 0:
				cur = cur + p
			p = p * b
			j = j+1
		has = 0
		for i in lp[b]:
			if cur % i == 0:
				s = s + ' ' + str(i)
				has = 1
				break
		if has == 0:
			return 0
	print s
	return 1
	
def main():
	lp[2].append(3)
	lp[2].append(715827883)
	
	lp[3].append(2)
	lp[3].append(6883)
	lp[3].append(22434744889)
	
	lp[4].append(5)
	lp[4].append(5581)
	lp[4].append(8681)
	lp[4].append(49477)
	lp[4].append(384773)
	
	lp[5].append(2)
	lp[5].append(3)
	lp[5].append(1303)
	lp[5].append(21207101)
	lp[5].append(28086211607)
	
	lp[6].append(7)
	lp[6].append(189491931189200021056951)
	
	lp[7].append(2)
	lp[7].append(373)
	lp[7].append(9754399)
	lp[7].append(5420506947192709)
	
	lp[8].append(3)
	lp[8].append(529510939)
	lp[8].append(715827883)
	lp[8].append(2903110321)
	
	lp[9].append(2)
	lp[9].append(5)
	lp[9].append(1403808961)
	lp[9].append(2860659169)
	lp[9].append(9500438809)
	
	lp[10].append(11)
	lp[10].append(909090909090909090909090909091)

	n = 32
	J = 500
	i = 1
	while ( i < (1<<25) ) and ( J > 0 ):
		if ok( i + (1<<31) ) == 1:
			J = J-1
		i = i+2

if __name__ == '__main__':
	main()
