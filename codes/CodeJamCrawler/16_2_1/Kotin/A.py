import os,sys,math
f = open('../input.txt',"r")
output = open('../output.txt',"w")
def out(t,sol):
	s = "Case #" + str(t+1) + ": " + str(sol)
	print(s)
	output.write(s + "\n")
T = int(f.readline())

a = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]

def deal(s,i,n):
	for c in a[i]:
		if c in s:
			j = s.index(c) if c in s else None
			del(s[j])
	n.append(str(i))

for t in range(0,T):
	s = list(f.readline())[:-1]
	n = []
	def func(i):
		deal(s,i,n)
	while 'Z' in s:
		func(0)
	while 'W' in s:
		func(2)	
	while 'U' in s:
		func(4)
	while 'X' in s:
		func(6)	
	while 'G' in s:
		func(8)
	while 'O' in s:
		func(1)	
	while 'H' in s:
		func(3)
	while 'S' in s:
		func(7)
	while 'V' in s:
		func(5)	
	while 'I' in s:
		func(9)
	n = sorted(n)
	num = ''.join(n)
	out(t,num)