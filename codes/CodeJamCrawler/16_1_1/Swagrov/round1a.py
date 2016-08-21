# read input
f = open('A-large.in','r')
small = f.read().split('\n')[1:-1]
f.close()

def val(s):
	return int(s,36)-10

def solve(s):
	r=s[0]
	for d in s[1:]:
		if val(d)>=val(r[0]):
			r = d + r
		else:
			r = r + d
	return r




# write output
file=open("anslarge.txt",'w')
case = 1
for i in small:
	file.write("Case #"+str(case)+': '+solve(i))
	file.write('\n')
	case += 1

file.close()
