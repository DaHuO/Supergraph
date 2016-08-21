f = open('B-large.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    pancake_stack = f.readline().strip()
    num_of_flips = 0
    for pancake in range(0, len(pancake_stack) - 1):
    	if pancake_stack[pancake] != pancake_stack[pancake + 1]:
    		num_of_flips += 1
    if pancake_stack[len(pancake_stack) - 1] == "-":
    	num_of_flips +=1
    s = "Case #%d: %s\n" % (t+1, num_of_flips)
    print s
    o.write(s)