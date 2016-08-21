t = input()

def flipState(lis):
	res = []
	for i in reversed(lis):
		if i=='+':
			res.append('-')
		else:
			res.append('+')
	return res

t1 = t
final = ""
while t:
	n = raw_input()
	inputLis = [i for i in n]
	result = 0
	l = len(inputLis)
	
	for i in xrange(l-1,-1,-1):
		if inputLis[i] == '-':
			if inputLis[0] == '-':
				inputLis[:i] = flipState(inputLis[:i+1])+inputLis[i+1:]
				result+=1
			else:
				for j in xrange(i-1, -1, -1):
					if inputLis[j]=='+':
						inputLis[:j]=flipState(inputLis[:j+1])+inputLis[j+1:]
						result+=1
						i+=1
						break
	final+="Case #{0}: {1}\n".format(t1-t+1, result)
	t-=1
print final
output_file = open('q2_small.out','w')
output_file.write("{}".format(final))
output_file.close()


			
	