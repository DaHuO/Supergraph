# google code jam shit
# author lee barnett
#
# i hate coding

import itertools

def iscomposite(n):
  if n == 2 or n == 3: return (False,0)
  if n < 2 or n%2 == 0: return (True,2)
  if n < 9: return (False,0)
  if n%3 == 0: return (True,3)
  r = int(n**0.5)
  f = 5
  while f <= r:
    #print '\t',f
    if n%f == 0: return (True, f)
    if n%(f+2) == 0: return (True, f+2)
    f +=6
  return (False,)   

def tobaseb(bintstr, b):
    n = 0
    for d in bintstr:
        n = b * n + int(d)
    return n

fin = open("input.txt","r")
fout = open("output.txt","w")

non = fin.readline()
notwon = fin.readline().strip()
twon = notwon.split()

N = int(twon[0])
J = int(twon[1])

found = 0

binstrings = [''.join(x) for x in itertools.product(['0','1'], repeat=N-2)]

binstrings = ['1' + curr +'1' for curr in binstrings]
#binstring = ["".join(thang) for thang in bintuples]

print binstrings

fout.write("Case #1:\n")

for bint in binstrings:

	#bint = int(bintstro)

	two = 0
	three = 0
	four = 0
	five = 0
	six = 0
	seven = 0
	eight = 0
	nine = 0
	ten = 0

	twoworks = False
	threeworks = False
	fourworks = False
	fiveworks = False
	sixworks = False
	sevenworks = False
	eightworks = False
	nineworks = False
	tenworks = False

	bout = tobaseb(bint, 2)
	out = iscomposite(bout)
	if out[0]: 
		twoworks = True
		two = out[1]

	bout = tobaseb(bint, 3)	
	out = iscomposite(bout)
	if out[0]:  
		threeworks = True
		three = out[1]

	bout = tobaseb(bint, 4)
	out = iscomposite(bout)
	if out[0]: 
		fourworks = True
		four = out[1]

	bout = tobaseb(bint, 5)
	out = iscomposite(bout)
	if out[0]: 
		fiveworks = True
		five = out[1]

	bout = tobaseb(bint, 6)	
	out = iscomposite(bout)
	if out[0]:  
		sixworks = True
		six = out[1]

	bout = tobaseb(bint, 7)
	out = iscomposite(bout)
	if out[0]: 
		sevenworks = True
		seven = out[1]

	bout = tobaseb(bint, 8)	
	out = iscomposite(bout)
	if out[0]:  
		eightworks = True
		eight = out[1]

	bout = tobaseb(bint, 9)
	out = iscomposite(bout)
	if out[0]: 
		nineworks = True
		nine = out[1]

	bout = tobaseb(bint, 10)	
	out = iscomposite(bout)
	if out[0]:  
		tenworks = True
		ten = out[1]
	
	if twoworks and threeworks and fourworks and fiveworks and sixworks and sevenworks and eightworks and nineworks and tenworks:
		fout.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(int(bint),two,three,four,five,six,seven,eight,nine,ten))
		found = found + 1
	
	if found == J: break;

fin.close()
fout.close()
