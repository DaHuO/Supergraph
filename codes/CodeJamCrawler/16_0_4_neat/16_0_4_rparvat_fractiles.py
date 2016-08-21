def answer(n):
	s=""
	for i in range(1,n):
		s+=str(i)+" "

	s+=str(n)
	return s

fileIn = "D-small-attempt1.in"
# fileIn = "random"
fileOut = "d_small_out.txt"
with open(fileIn, "r") as f:
	with open(fileOut, "w") as w:
		t = int(f.readline())
		for i in range(1,t+1):
			n = int(f.readline().split(" ")[0])
			w.write("Case #" + str(i)+": " + answer(n)+"\n")
