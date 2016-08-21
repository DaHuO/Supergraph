

def split_int_set(num):
	nums = str(num)
	nums = list(nums)
	nums = [int(x) for x in nums]
	nums = set(nums)
	return nums

def sleep_count(input):
	nums_seen = set([])
	nums_req = set([0,1,2,3,4,5,6,7,8,9])

	count = 0

	while(nums_req != nums_seen):
		count = count + 1
		nums_seen = nums_seen.union(split_int_set(count*input))
		

	return count*input;

inputs = []

f = open('p_a.txt', 'r')

for line in f:
    inputs.append(int(line))

f.close()

del inputs[0]

counter = 1

fx = open('outfile', 'w')

for i in inputs:
	if i == 0:
		fx.write("Case #"+str(counter)+": INSOMNIA\n")
	else:
		fx.write("Case #"+str(counter)+": "+str(sleep_count(i))+"\n")
	counter = counter + 1

