inp = open("pancake-large-inp.txt").read().split("\n")[1:-1]
out = open("pancake-large-out.txt", "w+")

def flip(x):
	x = x+"+";
	x = x[::-1]
	count = 0
	for i in range(1, len(x)):
		if x[i] != x[i-1]: count+=1
	return count


for i in range(len(inp)):
	out.write("Case #"+str(i+1)+": "+str(flip(inp[i]))+"\n")