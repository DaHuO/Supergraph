#!/usr/bin/python3

def main():
	f = open('../test_files/input', 'r')
	w = open('../test_files/output', 'w')
	s = f.readline()
	t = int(s)
	for i in range(1, t+1):
		w.write('Case #%d: ' % i)
		n = int(f.readline().strip())
		w.write(result(n) + '\n')

	w.close()
	
def result(n):
	if n == 0:
		return 'INSOMNIA'
	s = set()
	i = 0
	while True:
		i = i + 1
		s = s | set(list(str(n * i)))
		if len(s) == 10:
			return str(n * i)

if __name__ == '__main__':
	main()