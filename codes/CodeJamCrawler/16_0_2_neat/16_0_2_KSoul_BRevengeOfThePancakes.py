import sys

def flip(l):
	return [not i for i in l];

def revange_of_the_pancakes(argv):
	with open(argv[0], 'r') as f:
		t = int(f.readline())
		for i in range(t):
			s = f.readline().strip()
			ssize = len(s)

			a = 1
			happycookie = [True if x == '+' else False for x in s]
			#print s
			totalflip = 0 if happycookie[0] == True else 1;
			lastcookie = happycookie[0]
			while a < ssize:
				if(lastcookie == False):
					if lastcookie == happycookie[a]:
						pass
					else:
						lastcookie = True
				else:
					if lastcookie == happycookie[a]:
						pass
					else:
						totalflip = totalflip + 2
						lastcookie = False
				a = a + 1
			print "Case #%d: %d" % ((i+1), totalflip)

if __name__ == "__main__":
	revange_of_the_pancakes(sys.argv[1:])