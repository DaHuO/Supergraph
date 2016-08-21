# google code jam shit
# author lee barnett
#
# i hate coding

def solve(ins):
	havezero = False
	haveone = False
	havetwo = False
	havethree = False
	havefour = False
	havefive = False
	havesix = False
	haveseven = False
	haveeight = False
	havenine = False
	haveall = False

	copy = ins
	N = copy

	highest = 0

	if ins == 0:
		return "INSOMNIA"

#	while haveall is False:
	while True:
		inst = ins
		while inst > 0:
			mod = inst % 10
			#print mod
			if mod == 0:
				havezero = True
			elif mod == 1:
				haveone = True
			elif mod == 2:
				havetwo = True
			elif mod == 3:
				havethree = True
			elif mod == 4:
				havefour = True
			elif mod == 5:
				havefive = True
			elif mod == 6:
				havesix = True
			elif mod == 7:
				haveseven = True
			elif mod == 8:
				haveeight = True
			elif mod == 9:
				havenine = True
			inst = inst/10
			#print inst

		if haveone!=False and havetwo!=False and havethree!=False and havefour!=False and havefive!=False and havesix!=False and haveseven!=False and haveeight!=False and havenine!=False and havezero!=False:
			haveall = True
		highest = ins
		ins = copy + N
		copy = ins
		#print ins
		if haveall == True:
			break;
	return str(highest);


fin = open("input.txt","r")
fout = open("output.txt","w")

non = fin.readline()

k = 0

for line in fin.readlines():

	k = k+1
	if line.strip():
		currint = int(line)

	out = solve(currint)
	if k != int(non)+1:
		fout.write("Case #{0}: {1}\n".format(k, out))	

fin.close()
fout.close()
