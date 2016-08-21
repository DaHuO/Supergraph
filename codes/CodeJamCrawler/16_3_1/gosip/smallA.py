def main():
	f = open('A-large.in', 'r')
	t = int(f.readline())
	for i in range(t):
		ans = []
		n = int(f.readline())
		l = [int(x) for x in f.readline().strip().split()]	
		evacuate(l, ans)
		print('Case #' + str(i+1) + ': ' + ' '.join(ans))
	f.close()

def evacuate(l, ans):
	n = len(l)
	total = sum(l)
	
	if total == 0: 
		return

	idx1 = 0
	for i in range(n):
		curr = l[i]
		if curr > l[idx1]: 
			idx1 = i
	l[idx1] -= 1
	
	idx2 = 0
	for i in range(n):
		curr = l[i]
		if curr > l[idx2]: 
			idx2 = i
	if l[idx2] == 0 or total == 3:
		ans.append(chr(ord('A') + idx1))
	else:
		l[idx2] -= 1
		ans.append(chr(ord('A') + idx1) + chr(ord('A') + idx2))
	evacuate(l, ans)

if __name__ == '__main__':
	main()
