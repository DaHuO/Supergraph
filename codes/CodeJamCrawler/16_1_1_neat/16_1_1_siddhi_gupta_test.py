# def revNum (n, k):
# 	m = []
# 	for num in n:
# 		num = `num`[::-1]
# 		m.append(num)
# 	m.sort()
# 	print m
# 	ans = int(m[k-1][::-1])
# 	return ans
# n = [10,20,9,1000]
# k = 1
# t = revNum(n, k)
# print t
# from fractions import Fraction
# def solveEquation(s, r):
# 	posX_r = 0
# 	posX_s = 0
# 	if r.find("x"):
# 		posX_r = r.index("x")
# 		print posX_r
#     	coefX_r = int(r[:posX_r])
#     	posX_s = s.index("x")
#     	coefX_s = int((s[posX_s-2:posX_s]) if (posX_s > 1) else s[0])
#     	factor = str(Fraction (coefX_r / coefX_s) * -1)
#     	print factor
#     	print coefX_r % coefX_s
#     	#if str(factor).find("/"):
#     	if coefX_r % coefX_s != 0:
#     		factor_n = str(factor).split("/")[0]
#     		factor_d = str(factor).split("/")[1]
#     	else:
#     		factor_n = int(factor)
#     		factor_d = 1
#     	
#     	#print factor_d
#         posY_s = s.index("y")
#         coefY_s = int((s[posY_s-2:posY_s]) if (posY_s > 1) else s[0])
#         
#         disp_s = s.index("=")
#         dispV_s = int((s[disp_s-2:disp_s]))
#         dispV_s = 0 if 
#         print factor_n
#         print coefY_s
#         coefY_s = coefY_s * factor_n
#         print coefY_s
#         dispV_s = dispV_s * factor_n
#         print dispV_s
#         if str(dispV_s).find("-"):
#         	pass
#         else: 
#         	pass
#         	#dispV_s = "+" + str(dispV_s)
#         if factor_d ==1:
#         	print str(coefY_s)+"y"+str(dispV_s)
#         else:
#         	print str(coefY_s)+"y"+str(dispV_s)+"/"+str(factor_d)
#         
# s = "-4x+3y-12=0"
# r = "1x"
# solveEquation(s, r)

# import math
# def rewriteTheProduct(a, b, c, d):
#     list = []
#     num1 =0
#     num2 = 0
#     remainder = 0
#     def perfect_sq(n):
#     	print n
#         return n == int(math.sqrt(n)) ** 2
#     product = (math.pow(a, 2) + (math.pow(b, 2))) * (math.pow(c, 2) + (math.pow(d, 2)))
#     print product
#     bound = int(product / 8)
#     print bound
#     for i in range(bound):
#     	num1 = i
#         remainder = product - math.pow(num1, 2)
#         print remainder
#         if (remainder > 0):
# 			if perfect_sq(remainder):
# 				num2 = math.sqrt(remainder)
# 				if num1 < num2:
# 					list.append([num1, int(num2)])
#     return list
# 
# list = rewriteTheProduct(1,2,3,4)
# print list
'''
rewriteTheProduct = lambda a, b, c, d: [(i,j) for i in range(99) for j in range(i,99) if i*i+j*j==(a*a+b*b)*(c*c+d*d)]

def AirlineSeating(seats, premium, standard):
    list1 = []
    len1 = len(seats)
    print len1
    while len1 >=0:
        if premium > 0:
            list1.append('f')
            premium -= 1
            len1 -= 1
        elif standard > 0:
            list1.append('c')
            standard -= 1
            len1 -= 1
    return list1

list2 = AirlineSeating(["f", "f", "f", "c", "c", "c"], 2, 5)



def closestLocation(address, objects, names):
    def getSqrDistance(obj):
        if len(obj) == 2:
            return obj[0] * obj[0] + obj[1] * obj[1]
        if obj[0] == obj[2]:
            if obj[1] * obj[3] <= 0:
                return obj[0] * obj[0]
        else:
            if obj[0] * obj[2] <= 0:
                return obj[1] * obj[1]
        return min(obj[0] * obj[0] + obj[1] * obj[1],
                   obj[2] * obj[2] + obj[3] * obj[3])

    def isSimilar(str1, str2):
        differentChars = 0
        insertions = 0
        deletions = 0
        str1 = str1.lower()
        str2 = str2.lower()
        for i in range(len(str1)):
            if i >= len(str2) or str1[i] != str2[i]:
                differentChars += 1
        i = 0
        j = 0
        while i < len(str1):
            if j >= len(str2):
                insertions = 2
                break
            if str1[i] == str2[j]:
                i += 1
            else:
                insertions += 1
                if insertions > 1:
                    break
            j += 1
        i = 0
        j = 0
        while i < len(str1):
            if j < len(str2) :
                j += 1
            else:
                deletions += 1
            i += 1
        return differentChars <= 1 or insertions <= 1 or deletions <= 1

    bestIndex = -1
    bestDistance = 0
    for i in range(len(names)):
        if isSimilar(address, names[i]):
            sqrDistance = getSqrDistance(objects[i])
            if bestIndex == -1 or bestDistance > sqrDistance:
                bestDistance = sqrDistance
                bestIndex = i
    return names[bestIndex]


def perfectCity(departure, destination):
    result = 0
    for i in range(2):
        if math.floor(departure[i]) == math.floor(destination[i]):
            floorSum = departure[i] - math.floor(departure[i])
            floorSum += destination[i] - math.floor(destination[i])
            if floorSum < 1:
                result += floorSum
                departure[i] = math.floor(departure[i])
                destination[i] = math.floor(destination[i])
            else:
                result += 2 - floorSum
                departure[i] = math.ceil(departure[i])
                destination[i] = math.ceil(destination[i])
        else:
            if departure[i] > destination[i]:
                tmp = destination
                destination = departure
                departure = tmp
            result += math.ceil(departure[i]) - departure[i]
            departure[i] = math.ceil(departure[i])
            result += destination[i] - math.floor(destination[i])
            destination[i] = math.floor(destination[i])
        result += destination[i] - departure[i]

    return result
''''''
def numberOfKsBetween0AndN (n): 
    N = n
    p = 1
    i = 0
    c = 0
    while (n > 0):
    	d = n % 10
        n /= 10
        c += d * (p * i) / 10
        if (d > 4):
        	c += p
        elif (d == 4):
        	c += N % p 

        power *= 10
        i += 1
    return c
print numberOfKsBetween0AndN (14)

'''
'''def hailstoneLength( l):
	
    len1 = 0
    i = 0
    j = 0
    print l
    while(len1 != l):
        len1 = 0
        j = i
        print i 
        while(j != 1):
        	print j
        	if j % 2 == 0:
        		j /= 2
        	else: 
        		j = (3*j) + 1
            len1 += 1
    	print i
        i += 1
    return i
    
print hailstoneLength(350)'''



'''def sumOfPowers(n, divisor):
    print "l"
    total = 0
    for j in range(1, n):
        i = 0
        print "p"
        while 1:
        	print j
        	print i
        	if (divisor ** i) % j == 0:
        		print "true"
        		total += i
        		break
        	else:
        	    i += 1
    return total
    
    
print sumOfPowers(6, 2)

def circleOfNumbers(n, firstNumber):
    return (firstNumber + n/2)%n
'''
'''def differentValuesInMultiplicationTable(n, m):
    list1 = [[]]
    for i in range(0, n):
        for j in range(0, m):
            list1[i][j].append([i * j]) 
    print list1
differentValuesInMultiplicationTable(3, 2)'''

#num = 1234
#print list(str(num))
'''b = map(int, raw_input().strip().split(" "))

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = input()
for i in range(int(t)):
    l = int(input())
    num = input(l)
    print num
    k = 0
    for j in num:
        ind = num.index(j)
        left = sum[0:j]
        right = sum[j+1:l]
        if left == right:
                sys.stdout.write("YES")
                k = 1
    if not k:
        sys.stdout.write("NO")
  
for i in range(20, 1) :
	print i'''
'''import itertools
k = 4	
for i in itertools.product('GL', repeat=k):
	print i
'''
'''dict = {"b._la/np":	2}
print globals(dict)'''
'''import itertools
tags = ['DI', 'DD', 'DA', 'WW', 'FF', 'DT', 'DR', 'DP', 'PR', 'PP', 'PT', 'PX', 'NC', 'RG', 'PD', 'NP', 'RN', 'PI', 'VA', 'P0', 'CC', 'VM', 'AO', 'AQ', 'VS', 'ZZ', 'CS', 'II', 'START', 'END']
j = 0
for i in itertools.product(tags,repeat=2):
	j += 1
	print i[0]
	print i[1]
print j
'''
'''
transition = {'PP': {'START': 1, 'END': 2}}

prevTag = "PP"
key = prevTag
tag = "END"
value1 = 1
#print value
elementUpdated = False
if key not in (transition):
	transition.setdefault(key, {})
	transition[key][tag] = (value1)
else:
	#print transition
	for element in transition[key]:
		print element
		if tag == element:
			elementUpdated = True
			transition[key][tag] += 1
			break
	if not elementUpdated:
		transition[key][tag] = (value1)
print transition
'''
'''
transition = {'PP': [{'START': 1}, {'END': 2}]}
tags = {"PP": "PS"}
print tags.keys()[0]
key = "PP"
for tag, keys in zip(tags, transition[key]):
	print tag
	print key
'''
'''import itertools
from itertools import permutations
lst = range(1, 11)
print(list(itertools.product(lst, repeat=2)))
def combi():
	iterable = range(1, 11)
	for comb in permutations(iterable, 2):
		yield comb	
gen = combi()
for i in gen:
	print i
'''
def lastWord(str):
	newStr = ""
	for letter in str:
		print letter
		if newStr == "":
			newStr += letter
		elif letter >= newStr[0]:
			newStr = letter + newStr
		else:
			newStr += letter
	print newStr
	return newStr
			
f = open("A-large.in", 'r')
f1 = open("output.txt", 'w')
noTestcases = int(f.readline())
for j in range(noTestcases):
    ans = lastWord(f.readline())
    f1.write("Case #" + str(j + 1) + ": " + ans)
	