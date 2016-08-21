#Coin Jam
T= input()
x = raw_input()
a = int(x.split()[0])
b = int(x.split()[1])
cnt = 0

print "Case #1:"
for i in open('allNonPrimes.txt'):
	if(len(i.split()[0]) == a):
		print i,
		cnt += 1
	if(cnt>=b):
		break