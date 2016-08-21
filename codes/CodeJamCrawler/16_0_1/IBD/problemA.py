import re
def findAllDig(n):
	dig = set([])
	while n>0:
		dig.add(n%10)
		n = n/10
	return dig

def tillAll(n):

	s = findAllDig(n)
	all_n = set(range(0,10))
	if s == all_n :
		return n
	for i in range(2,100000):
		s = s.union(findAllDig(i*n)) 
		if s == all_n :
			return i*n
	return "INSOMNIA"

#print tillAll(1692)

def read_input(input1,output):
	o = open(input1,"r")
	w = open(output,"w")
	l = o.readline()
	num_of_cases =  int(re.findall(r'[0-9]+',l)[0])
	for i in range(1,num_of_cases+1):
		l = o.readline()
		L = int(re.findall(r'[0-9]+',l)[0])
		w.write("case #%d: %s\n" %((i),str(tillAll(L))))
	w.close()
if __name__ == "__main__":
	read_input("A-large.in","outputAL.out")

