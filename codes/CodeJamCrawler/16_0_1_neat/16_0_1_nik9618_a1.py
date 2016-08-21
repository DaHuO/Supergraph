f = open('/Users/nik9618/Downloads/A-large.in', 'r')
case = 1
f.readline()
for line in f.readlines():

	i = int(line.split('\n')[0])
	if(i==0) : 
		print 'Case #'+str(case)+': INSOMNIA'
		case +=1
		continue;

	x = [0,0,0,0,0,0,0,0,0,0];
	total = 0;

	ct  = 1
	while True:
		tmp = i * ct
		while(tmp>0):
			if(x[tmp%10] == 0):
				total = total+1
				x[tmp%10]=1
			tmp = tmp/10
		if(total == 10):
			break;
		ct = ct + 1
		
	print 'Case #'+str(case)+': '+str(i*ct)
	case+=1

