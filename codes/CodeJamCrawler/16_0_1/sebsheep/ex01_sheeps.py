from itertools import count, islice

def last_count(n):
	seen = [False] * 10
	for i in islice(count(),1, None):
		for j in map(int, str(i*n)):
			seen[j] = True
		if all(seen):
			return i * n

def print_res(values, file):
	for i, n in enumerate(values):
		print("Case #%d:"%(i+1), end=" ", file=file)
		if n == 0:
			print("INSOMNIA", file=file)
		else:
			print(last_count(n), file=file)

if __name__ == "__main__":
	n = int(input())
	with open("/tmp/out_largeA.txt", "w") as out:
		print_res((int(input()) for _ in range(n)), out)