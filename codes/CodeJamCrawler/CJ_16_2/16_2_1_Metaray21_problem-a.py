#    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
mapping = [
	[0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
	[0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0],
	[0,0,0,0,2,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
	[0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0],
	[0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
	[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
	[0,0,0,0,2,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0],
	[0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
	[0,0,0,0,1,0,0,0,1,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0],
]

order = [(8, 'G'), (4, 'U'), (2, 'W'), (6, 'X'), (0, 'Z'), (1, 'O'), (3, 'R'), (7, 'S'), (5, 'F'), (9, 'I')]

# 8 - G
# 4 - U
# 2 - W
# 6 - X
# 0 - Z
# 1 - O
# 3 - R
# 7 - S
# 9 - N
# 5 - E

data = open("A-large.in").readlines()
data = map(lambda x: x.strip(), data)

n = int(data[0])
answ = []

for i in xrange(n):
	s = data[i+1]
	chars = [0]*26
	for c in s:
		#print c
		chars[ord(c)-ord('A')] += 1
	#print '!',chars 
	nums = [0]*10
	for nm, ch in order:
		ch = ord(ch) - ord('A')
		nums[nm] = chars[ch]
		for k in xrange(26):
			chars[k] -= mapping[nm][k]*nums[nm]
	pts = []
	for j,k in enumerate(nums):
		if k > 0:
			pts.append(str(j)*k)
	answ.append("".join(pts))

with open("A-large.out", 'w') as f:
	for i,s in enumerate(answ):
		f.write("Case #{}: {}\n".format(i+1, s))
