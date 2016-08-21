

nums = [l.strip() for l in open('input.txt')]
nums = nums[1:]

f = open('output.txt','w')
i = 0

for num in nums:
	i = i+1
	count = 0
	lastpc = 0
	for pc in list(num): 
		if lastpc == 0:
			lastpc = pc
		else:
			if pc != lastpc:
				count = count + 1
				lastpc = pc

	if list(num)[-1]=='-':
		count = count + 1

	f.write('Case #')
	f.write(str(i))
	f.write(': ')
	f.write(str(count))
	f.write('\n')

f.close()