import numpy as np

ndigits = 16 # Half of
ncounts = 500

powers = np.ndarray((11,), dtype="uint64")
spowers = ""
for n in range(2, 11):
	powers[n] = n ** ndigits + 1
	spowers += " " + str(powers[n])

def num2strby2(n, length):
	res = ""
	while n > 0:
		res = str(n % 2) + res
		n = n // 2
	return res.zfill(length)

with open("c-large.txt", "w") as f:
	f.write('Case #1:\n' + '\n'.join(['1' + num2strby2(ntry, ndigits - 2) + '11' + num2strby2(ntry, ndigits - 2) + '1' + spowers for ntry in range(ncounts)]))