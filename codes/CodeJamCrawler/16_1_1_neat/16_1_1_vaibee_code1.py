with open("ip.txt","r") as fo:
	t=int(fo.readline())
	p=1
	with open("op.txt","a") as output:
		while p<=t:
			word=fo.readline()
			li=[]
			st2=""
			for x in word:
				if len(li)==0 or x<li[0]:
					li.append(x)
				else:
					li=[x]+li
			st2=''.join(li).strip()
			output.write("Case #%d: %s\n"%(p,st2))
			p=p+1