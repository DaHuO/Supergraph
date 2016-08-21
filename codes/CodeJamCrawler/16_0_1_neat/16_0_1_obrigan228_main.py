n = int(input())
def check(has):
	for k in has:
		if not k:
			return False
	return True
for i in range(1,n+1):
	has = [False]*10
	t = input()
	if t =='0':
		print('Case #{}: INSOMNIA'.format(i))
		continue
	k = int(t)
	v = k
	s = set(list(t))
	for el in s:
		has[int(el)]=True
	while not check(has):
		v+=k
		t=str(v)
		s = set(list(t))
		for el in s:
			has[int(el)]=True

	print('Case #{}: {}'.format(i,v))