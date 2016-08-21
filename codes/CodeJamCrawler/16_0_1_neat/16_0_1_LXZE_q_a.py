f = open("A-small-attempt0.in","r")
w = open("output_a.txt","w")
num = f.readline()
for it in range(0,int(num)):
	res = ''
	num = int(f.readline())
	if num == 0:
		res = 'INSOMNIA'
	else:
		idx = 0
		txt = ''
		val = num
		found = False
		while idx<100:
			txt += str(val)
			if(len(set(str(txt)))<10):
				val += num
				idx+=1
			else:
				res = val
				found = True
				break
		if not found:
			res = 'INSOMNIA'
	print("Case #{0}: {1} ".format(it+1,res))
	w.write("Case #{0}: {1}\n".format(it+1,res))
w.close()