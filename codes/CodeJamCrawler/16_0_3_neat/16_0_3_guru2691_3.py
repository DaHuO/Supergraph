T = input()
N, J = map(int, raw_input().split())

n = ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1']
odd = range(1, 30, 2)
even = range(2, 31, 2)

twoOnes = [(x, y) for x in odd for y in even]
fourOnes = [(w, x, y, z) for w in odd for x in odd for y in even for z in even if (x > w) and (y > z)]
divisors = ['3', '4', '5', '6', '7', '8', '9', '10', '11']

print "Case #1: "
count = 1
print "".join(n) + " " + " ".join(divisors)

for points in twoOnes:
	n[points[0]] = '1'
	n[points[1]] = '1'
	print "".join(n) + " " + " ".join(divisors)
	count += 1
	n[points[0]] = '0'
	n[points[1]] = '0'

for points in fourOnes:
	if count == 500:
		break
	n[points[0]] = '1'
	n[points[1]] = '1'
	n[points[2]] = '1'
	n[points[3]] = '1'
	print "".join(n) + " " + " ".join(divisors)
	count += 1
	n[points[0]] = '0'
	n[points[1]] = '0'
	n[points[2]] = '0'
	n[points[3]] = '0'
