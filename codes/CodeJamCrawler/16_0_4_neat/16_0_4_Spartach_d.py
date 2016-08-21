LOG_FILE = "D-small-attempt1.in"

with open(LOG_FILE) as f:
	data = f.readlines()

g = open("d.txt", "wb")

ntimes = int(data[0])
for ntry in range(ntimes):
	k, c, s = [int(i) for i in data[ntry + 1].split()]
	step = k ** (c - 1)
	g.write("Case #" + str(ntry + 1) + ": " + " ".join([str(1 + i * step) for i in range(k)]) + "\n")

g.close()