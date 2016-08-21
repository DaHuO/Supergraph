from __future__ import division
import math

def int2base(x, base):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

def divider(num):
	print num
	to = int(math.sqrt(num)) + 1
	for x in range(2, to):
		if num % x == 0:
			return x
	return None

g = open("output.out", 'w')
j = 50
i = 0

dos = None
tres = None
cuatro = None
cinco = None
seis = None
siete = None
ocho = None
nueve = None
diez = None

init = 32769
end = 65535

g.write("Case #1:\n")

for x in range (init, end + 1):

	if i >= j:
		break
	if bin(x)[2] != "1" or bin(x)[17] != "1":
		continue

	print i
	print x

	dos = divider(int(bin(x)[2:],2))
	if not dos:
		continue
	tres =  divider(int(bin(x)[2:],3))
	if not tres:
		continue
	cuatro = divider(int(bin(x)[2:],4))
	if not cuatro:
		continue
	cinco = divider(int(bin(x)[2:],5))
	if not cinco:
		continue
	seis = divider(int(bin(x)[2:],6))
	if not seis:
		continue
	siete = divider(int(bin(x)[2:],7))
	if not siete:
		continue
	ocho = divider(int(bin(x)[2:],8))
	if not ocho:
		continue
	nueve = divider(int(bin(x)[2:],9))
	if not nueve:
		continue
	diez = divider(int(bin(x)[2:],10))
	if not diez:
		continue
	i = i + 1
	g.write(bin(x)[2:] + " " + str(dos) + " " + str(tres) + " " + str(cuatro) + " " + str(cinco) + " " + str(seis) + " " + str(siete) + " " + str(ocho) + " " + str(nueve) + " " + str(diez) + "\n")

# while i<cases:
# 	print "-----------"
#  	i = i+1
# 	dinners = int(f.readline())
# 	pancakes = f.readline()
# 	pancakesList = pancakes.split()
# 	for x in range(0,dinners):
# 		print pancakesList[x]
# 		pancakesList[x] = int(pancakesList[x])

# 	result = fun(pancakesList)
# 	print result
# 	g.write("Case #" + str(i) + ": " + str(result) + "\n")








	
