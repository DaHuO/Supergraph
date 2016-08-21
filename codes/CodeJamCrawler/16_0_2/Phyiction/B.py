
def flip(stack,i):
	tmp = []
	a = stack[0:i+1]
	for j in a:
		if j == '+':
			tmp.append('-')
		else:
			tmp.append('+')
		#end
	#end for
	tmp.reverse()
	return  tmp + stack[i+1:]
#end flip

# all pancakes happy side up
def min_flips(stack, flips):
	#print stack
	if ''.join(stack) == '+'*len(stack):
		return flips
	elif ''.join(stack) == '-'*len(stack):
		return flips + 1
	else:
		i = 1
		while i < len(stack) and stack[i] == stack[i-1]:
			i = i + 1
		#end while
		return min_flips(flip(stack,i-1),flips+1)
	#end if
#end min_flips

if __name__ == "__main__":
	T = int(raw_input())
	for i in range(T):
		stack = list(raw_input())
		print "Case #{0}: {1}".format(i+1,min_flips(stack,0))
	#end for
#end if