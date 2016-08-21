import itertools
from itertools import combinations

EMPTY = "IMPOSSIBLE"


def get_fractile_nums(k, c, s):
	org_list = []
	fractile_list = []

	if k == s:
		return (str(j+1) for j in range(s))


	if c == 1:
		if k == s:
			return (str(j+1) for j in range(s))
		if k > s:
			return EMPTY

	for o in itertools.product(["G", "L"], repeat=(k)):
		org = "".join(o)
		org_list.append(org)
		fractile = make_fractile(org, c)
		fractile_list.append(fractile)

	# print(fractile_list)
	# s는 while 문 돌면서 하나씩 증가 시킴
	s_count = 1
	while s >= s_count:
		index_items = (str(i+1) for i in range(k**c))
		result = select_clean_nums(org_list, fractile_list, index_items, s_count)
		if result is not None and len(result) > 0:
			# print(result)
			return result
		s_count += 1
	return [EMPTY]


def make_fractile(org, c):
	target_tile = org
	for i in range(int(c)-1):
		fractile = ""
		for c in target_tile:
			if c == 'L':
				fractile += org
			else:
				for i in range(len(org)):
					fractile += "G"
		target_tile = fractile
	return target_tile


def select_clean_nums(org_list, fractile_list, index_items, s_count):
	for c in combinations(index_items, s_count):
		success_flag = False
		for f in range(len(fractile_list)):
			part_fractile = ""
			for p in c:
				part_fractile += fractile_list[f][int(p)-1]

			# L이 나왔으면, org을 확인하여 G가 있는지 확인, 없다면, 끝
			# 있다면, s 개수의 조합만큼 찾아서 확인
			if 'G' not in part_fractile:
				success_flag = 'G' not in org_list[f]
				if not success_flag:
					break

		if success_flag:
			return c

	return None


t = int(input())
for i in range(1, t + 1):
	k, c, s = [int(a) for a in input().split(" ")]
	print("Case #{}: {}".format(i, " ".join(get_fractile_nums(k, c, s))))
