import sys

def normalize_cakes(cakes):
	norm_cakes = ""
	for i in range(len(cakes)):
		if i == 0:
			norm_cakes = norm_cakes + cakes[i]
		else:
			if cakes[i] != cakes[i-1]:
				norm_cakes = norm_cakes + cakes[i]

	return norm_cakes

def calc_flips(cakes):
	cakes = normalize_cakes(cakes)
	num_flips = 0
	
	for i in range(len(cakes)):
		if cakes[i] == "-":
			if i == 0:
				num_flips += 1
			else:
				num_flips += 2

	return num_flips

def main():
	n = int(raw_input())

	for i in range(n):
		cakes = raw_input()
		num_flips = calc_flips(cakes)
		print "Case #%d: %d" %(i+1, num_flips)

if __name__ == "__main__":
	main()
