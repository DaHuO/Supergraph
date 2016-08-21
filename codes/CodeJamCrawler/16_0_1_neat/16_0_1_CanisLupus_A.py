def main():
	for TEST in xrange(1, int(raw_input())+1):
		N = int(raw_input())

		if N == 0:
			print "Case #%d: INSOMNIA" % (TEST)
			continue

		unseenDigits = set(chr(ord('0')+i) for i in xrange(0,10))
		num = 0

		while len(unseenDigits) > 0:
			num += N
			for d in str(num):
				if d in unseenDigits:
					unseenDigits.remove(d)

		print "Case #%d: %s" % (TEST, str(num))

main()
