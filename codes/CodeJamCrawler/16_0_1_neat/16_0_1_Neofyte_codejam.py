def checknumber(n):
	sofar, i, lastN, mustContain = [], 1, 0, list(range(10))
	while sofar != mustContain:
		if i > 10000:
			return "INSOMNIA"
		lastN = i*n
		for s in map(lambda x: int(x), list(str(lastN))):
			if s not in sofar:
				sofar.append(s)
		sofar.sort()
		i += 1
	return lastN

def main():
    out = []
    inp = open("large.in", "r")
    ncases = int(inp.readline())
    for i in range(ncases):
    	out.append(int(inp.readline()))

    outfile = open("out.txt", "w")
    for n in range(len(out)):
    	outfile.write("Case #"+str(n+1)+": "+str(checknumber(out[n]))+"\n")

main()    
