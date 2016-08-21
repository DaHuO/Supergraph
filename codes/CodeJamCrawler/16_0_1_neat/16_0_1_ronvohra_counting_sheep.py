inp = [line.rstrip('\n') for line in open ('A-small-attempt1.in')]
n = int(inp[0])
ans_list = []
for i in range(n):
	num_str_canon = inp[i + 1]
	set_canon = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
	seen_list_canon = [int(elem) for elem in num_str_canon]
	seen_list_canon = list(set(seen_list_canon))
	seen_list = seen_list_canon[:]

	if set(seen_list) == set_canon:
		ans = int(num_str_canon)
		ans_list.append("Case #{0}: {1}\n".format(i+1, ans))
	else:
		mult = 2
		while True:
			num_str = mult*int(num_str_canon)
			seen_temp = [int(elem) for elem in str(num_str)]
			seen_list.extend(seen_temp)
			if set(seen_list) == set_canon:
				ans = int(num_str)
				ans_list.append("Case #{0}: {1}\n".format(i+1, ans))
				break
			elif set(seen_list) == set(seen_list_canon):
				ans_list.append("Case #{}: INSOMNIA\n".format(i+1))
				break
			else:
				mult += 1
				continue

with open('counting_sheep_small.out', 'w') as f:
	for item in ans_list:
		f.write(item)
