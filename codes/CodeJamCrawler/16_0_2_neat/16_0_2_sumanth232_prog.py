from sets import Set
import time


t = input()
for tc in range(t):
	s  = raw_input()
	print 'Case #{}:'.format(tc+1),

	cnt = 0

	while '-' in s:
		s = s.rstrip('+')
		# print s
		if s[0] == '-':
			s = s.replace('-','t')
			s = s.replace('+','-')
			s = s.replace('t','+')
			s = s[::-1]
			cnt += 1
		else:
			leading_pluses_len = s.find('-')
			s = ('-'*leading_pluses_len) + s[leading_pluses_len:]
			cnt += 1

	print cnt


