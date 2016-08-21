tc = int(input())
for i in range(1,tc+1):
	ans1 = 'Case #'+str(i)+': ';
	a = int(input())
	count = 0;
	match = [0] * 10;
	mulfac = 1;
	ans = 0;
	while count < 10:
		res = mulfac * a;
		t = res;
		if res == a and mulfac != 1:
			ans = 'INSOMNIA'
			break;
		else:
			while t != 0:
				r = t % 10;
				t = t // 10;
				if match[r] != 1:
					count = count + 1;
					match[r] = 1;
		mulfac += 1;
	if ans == 0:
		ans = res;
	ans1 += str(ans);
	print(ans1);
