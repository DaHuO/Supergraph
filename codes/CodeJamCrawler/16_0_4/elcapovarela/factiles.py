f = open("fractilesSmall.in", "r")
new_file = open("factilesSmallSol", "w")
t = int(f.readline())

for i in range(1,t+1):
	k,c,s = [int(x) for x in f.readline()[:-1].split(" ")]
	fractiles_to_see = " ".join([str(x) for x in range(1,s+1)])
	new_file.write("Case #"+str(i)+ ": "+fractiles_to_see+"\n")
