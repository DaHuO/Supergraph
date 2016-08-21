import re, json

def count_digits(N):
	n = N
	if n == 0:
		return 'INSOMNIA'
	#end if
	seen = {}
	i = 1
	while len(seen.keys()) != 10:
		for t in str(i*n):
			if t not in seen:
				seen[t] = 1
			else:
				seen[t] = seen[t] + 1
			#end if
		#end for
		i = i + 1
	#end while
	#print json.dumps(seen,indent=2)
	
	return (i-1)*N
#end if

if __name__ == "__main__":
	T = int(raw_input())
	for i in range(T):
		N = int(raw_input())
		print "Case #{0}: {1}".format(i+1,count_digits(N))
	#end for
#end if