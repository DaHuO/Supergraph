# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import itertools

f = open('C-large.in', 'r')
fout = open('C-large.out', 'w')
t = int(f.readline().split()[0])  # read a line with a single integer

def get_tuples_list(N):
        odd_list = [x for x in itertools.combinations(range(1,N-1,2),2)]
	even_list = [x for x in itertools.combinations(range(2,N,2),2)]
	tuples_list = [(x,y) for x in odd_list for y in even_list]
	return tuples_list
def get_tuple_jamcoin(N, index_tuple):
	tmp = '1' + '0'*(N-2) + '1'
	res = '' 
	x, y = index_tuple
	xe1 = x[0]
	xe2 = x[1]
	yo1 = y[0]
	yo2 = y[1]

	for i in range(N):
		if i==xe1 or i==xe2 or i==yo1 or i==yo2:
			res += '1'
		else:
			res += tmp[i]
        print x, y, res
	return res

def jamcoin_to_num(s, base):
	res = 0
        for i in range(len(s)-1,-1,-1):
		tmp = int(s[i])
                res = base *(res + int(s[i]))
	res = res/base
	return res
	


for i in xrange(1, t + 1):
  inlist  = f.readline().split() # read a list of integers, 2 in this case
  N = int(inlist[0])
  J = int(inlist[1])
  tuples_list = get_tuples_list(N)
  divstr = ""
  for k in range(2,11):
	  divstr += str(k+1)
	  divstr += " "
  divstr +="\n"
  outstr =  "Case #" + str(i) + ": " + "\n"
  res = ""
  res_set = set([])
  for count in range(J-1):
	  tl = tuples_list[count]
	  jamcoin = get_tuple_jamcoin(N,tl)
	  res_set.add(jamcoin)
	  res += jamcoin
	  res += " "
	  res += divstr
	  for q in range(2,11):
		  jnum = jamcoin_to_num(jamcoin, q)
		  if jnum%(q+1):
			  print "Fail!!!", jamcoin, jnum, q
  basecase = '1' + '0'*(N-2) + '1'
  res += basecase + " " + divstr
  outstr += res
  fout.write(outstr)
  print outstr
  print "Num of Distinct jamcoins = ", len(res_set) + 1
  # check out .format's specification for more formatting options


f.close()
fout.close()

