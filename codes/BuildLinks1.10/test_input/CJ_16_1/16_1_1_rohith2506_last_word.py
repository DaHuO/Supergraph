def last_word(inp):
	result = inp[0]
	for i in range(1, len(inp)):
		temp1 = result + inp[i]
		temp2 = inp[i] + result
		result = max(temp1, temp2)
	return result

if __name__ == "__main__":
	t = int(raw_input())
	for i in range(1, t+1):
		inp = raw_input()
		result = last_word(inp)	
		print "Case #%d: %s" %(i, result) 
