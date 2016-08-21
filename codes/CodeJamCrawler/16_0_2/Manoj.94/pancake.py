class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.insert(0,item)

     def pop(self):
         return self.items.pop(0)

     def peek(self):
         return self.items[0]

     def check(self):
     	if "-" in self.items:
     		return True
     	else: return False


def flip(string):
	for i in range(len(string)):
		if string[i] == '+':
			string[i] = '-'
		else:
			string[i] = '+'
	return string


f = open("input","r+")
o = open("output","w+")
line = f.readlines()

for i in range(int(line[0])):
	val = line[i+1]
	val = val[::-1]
	s = Stack() 
	for w in val:
		if w != '\n':
			s.push(w)
	
	count = 0
	while s.check():
		temp = []	
		if s.peek() == '-':
			while s.peek() != '+':
				temp += s.pop()
				if s.isEmpty() == True:
					break
			temp = flip(temp)
			for w in temp:
				s.push(w)
		elif s.peek() == '+':
			while s.peek() != '-':
				temp += s.pop()
				if s.isEmpty() == True:
					break
			temp = flip(temp)
			for w in temp:
				s.push(w)
		count = count + 1	

	o.write("Case #%d: %d\n" % (i+1,count))
f.close()
o.close()
