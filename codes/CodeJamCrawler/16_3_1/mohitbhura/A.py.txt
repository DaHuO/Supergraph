t = int(raw_input())
for _ in xrange(t):
	n = int(raw_input())
	arr = map(int,raw_input().split())
	total = sum(arr)
	m = max(arr);
	ans = 'Case #'+str(_+1)+': ';
	while total > 0 :
		m = max(arr)
		flag = 0;
		for i in xrange(n):
			if flag == 2 : 
				break;
			if arr[i] == m :
				total -= 1;
				ans+=chr(i+65)
				arr[i]-=1;
				flag+=1;
		ans += ' ';
	print ans;