for tc in range(input()):
	master_list = ""
	for i in range(2 * input() - 1):
		master_list = master_list + " " + raw_input()
	master_list = master_list.split()
	counter_dict = dict((x,master_list.count(x)) for x in set(master_list))
	ans = []
	for i in counter_dict:
		if counter_dict[i] % 2 == 1:
			ans = ans + [int(i)]
	ans = sorted(ans)
	final_ans = ""
	for i in ans:
		final_ans = final_ans + " " + str(i)
	print "Case #" + str(tc+1) + ":" + final_ans