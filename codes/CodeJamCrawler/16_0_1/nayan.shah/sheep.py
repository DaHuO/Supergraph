def answer(n):
	if n == 0:
		return 'INSOMNIA'
	seen = set(str(n))
	
	last = n
	while len(seen) != 10:
		last += n
		seen = seen | set(str(last))
	return str(last)
  

def main():
    total = input()
    data = [input() for i in range(total)]
    res = map(answer, data)
    for (i, ans) in enumerate(res):
        print 'Case #%d: %s' % (i+1, ans)

if __name__ == "__main__":
	main()
