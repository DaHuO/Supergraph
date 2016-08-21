from sets import Set

nums = [int(l.strip()) for l in open('input.txt')]
nums = nums[1:]

all_digits = Set(['1', '0', '3', '2', '5', '4', '7', '6', '9', '8'])

f = open('output.txt','w')
i = 0

for num in nums:
	i = i+1
	digits = Set([])
	n = 0
	if num == 0:
		n = 'INSOMNIA'
	else:
		while not digits.issuperset(all_digits):
			n = n + num
			digits.update(Set(list(str(n))))
	f.write('Case #')
	f.write(str(i))
	f.write(': ')
	f.write(str(n))
	f.write('\n')

f.close()