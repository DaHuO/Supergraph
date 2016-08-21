
import math

def solveD(k,c,s):
	return " ".join([str(j) for j in range(1,k+1)])

if __name__ == "__main__":
	# ip_fname = "D-ex.in"
	ip_fname = "D-small-attempt3.in"
	# op_fname = "D-ex.out2"
	op_fname = "D-small-attempt3.out"
	ip = open(ip_fname, 'r')
	op = open(op_fname , 'w')

	t = int(ip.readline())
	for tc in range(t):
		ip_line = ip.readline()
		# print(ip_line)
		k,c,s = map(int,ip_line.split(" "))
		op.write("Case #"+str(tc+1)+": "+str(solveD(k,c,s))+"\n")

	ip.close()
	op.close()