
def flip(s,s_len):

	list_s = list(s)
	for i in range(s_len/2):
		tmp=list_s[i]
		list_s[i] = list_s[s_len-1-i]
		list_s[s_len-1-i]=tmp

	for i in range(s_len):
		if list_s[i] == '-':
			list_s[i]='+'
		else:
			list_s[i]='-'

	return ''.join(list_s)
	

for t in range(input()):
	s = raw_input()
	s_len = len(s)

	#print s
	#print flip(s,4)

	dict_s = dict()
	dict_s[s] = 1

	q_s = list()
	q_len = list()

	q_s.append(s)
	q_len.append(0)

	q_head = 0
	ans = 0

	#Exceptional Case when it is already done
	if (s.find('-') == -1):
		q_head = 1

	while q_head < len(q_s) and ans == 0:

		for i in range(s_len):
			flip_s=flip(q_s[q_head],1+i)

			if (flip_s.find('-') == -1):
				ans = q_len[q_head]+1
				break

			if not (flip_s in dict_s):
				dict_s[flip_s] = 1

				q_s.append(flip_s)
				q_len.append(q_len[q_head]+1)

		q_head += 1

	print "Case #%d: %s" %(t+1,ans)



