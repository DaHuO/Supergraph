def flip(panstack):
	fstack=""
	for cake in list(panstack):
		if cake=="+":
			fstack="-"+fstack
		elif cake=="-":
			fstack="+"+fstack
	return fstack

def flipnumber(panstack):
	if panstack=="+":
		return 0
	elif panstack=="-":
		return 1
	elif panstack.endswith("+"):
		return flipnumber(panstack[:-1])
	elif panstack.endswith("-") and panstack.startswith("-"):
		return 1+flipnumber(flip(panstack))
	elif panstack.endswith("-") and panstack.startswith("+"):
		numplus=panstack.find("-");
		return 1+flipnumber(flip(panstack[0:numplus])+panstack[+numplus:])
	


t = int(input()) 
for i in range(1, t + 1):
	print("Case #{}: {}".format(i,flipnumber(input())))