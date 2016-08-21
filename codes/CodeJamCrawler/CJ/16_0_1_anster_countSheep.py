import timeit
start = timeit.default_timer()

def calculate(value,count):
	tlist = int(value)
	i = 1
	dlist=list()
	if tlist == 0:
		result = 'INSOMNIA'
	else:
		while(len(dlist) < 10):
			num = tlist * (i)
			number_string = str(num)
			for ch in number_string:
				if(ch not in dlist):
					dlist.append(ch)
			i = i + 1
		result = num
	logfile = open('sheepOutput.txt', 'a')
	logfile.write('Case #%s: %s\r\n' % (count,result))
	logfile.close()

fname = 'sheepInput.txt'
with open(fname) as f:
    content = f.readlines()
count = 0
tempcount = 1
logfile = open('output.txt', 'w')
logfile.write('')
logfile.close()

for r in content:
	if count == 0:
		pass
	else:
		calculate(r,count)
	count = count + 1
stop = timeit.default_timer()
print stop - start