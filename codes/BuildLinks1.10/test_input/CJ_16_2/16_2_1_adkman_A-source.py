dic = {0:'ZERO',1:"ONE", 2:"TWO",3:"THREE",4:"FOUR",5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE'}
def rep(s, lis):
	for i in lis:
		s = s.replace(i, '', 1)
	return s

T = int(input())
for i in range(1, T+1):
	ans = []
	s = input()

	while 'Z' in s:
		ans.append(0)
		s = rep(s, dic[0])

	while 'W' in s:
		ans.append(2)
		s = rep(s, dic[2])

	while 'U' in s:
		ans.append(4)
		s = rep(s, dic[4])

	while 'X' in s:
		ans.append(6)
		s = rep(s, dic[6])

	while 'G' in s:
		ans.append(8)
		s = rep(s, dic[8])

	while 'H' in s:
		ans.append(3)
		s = rep(s, dic[3])

	while 'F' in s:
		ans.append(5)
		s = rep(s, dic[5])

	while 'V' in s:
		ans.append(7)
		s = rep(s, dic[7])

	while 'O' in s:
		ans.append(1)
		s = rep(s, dic[1])

	while 'I' in s:
		ans.append(9)
		s = rep(s, dic[9])

	ans.sort()

	print('Case #'+str(i)+': ', end='')
	for x in ans:
		print(str(x),end='')
	print('')



