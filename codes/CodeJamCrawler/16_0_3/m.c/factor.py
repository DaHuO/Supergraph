import itertools
from functools import reduce

def factors(n):    
	return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def getVals(jamcoin):
	results = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(len(jamcoin)):
		# 2, 3, 4, 5, 6, 7, 8, 9, 10
		for j in range(9):
			results[j] += int(jamcoin[-(i+1)])* ( (j+2)**i)
		# print(results)

	return results 

def getBins(len):
	r = []
	res = ["".join(seq) for seq in itertools.product("01", repeat=len-2)]
	for i in res:
		a = "1" + str(i) + "1"
		r.append(a)
	return r

def checkAllNotPrimes(tab):
	ans = True
	results = []
	for i in tab:
		aa = factors(i)
		if len(aa)<3:
			ans = False
			return ans, aa
		aa.sort()
		results.append(i/aa[1])

	return ans, results

def getDivs(nums):
	jamVals = []
	for jamcoin in nums:
		x = getVals(jamcoin)
		jamVals.append(x)
		hue = checkAllNotPrimes(x)
		if(hue[0] ):
			res = jamcoin + " "
			for i in hue[1]:
				res += (str(int(i))+" ")
			print(res)


nums = getBins(16)
print(len(nums))

print("Case #1:")
getDivs(nums)




# r = getVals('100011')
# for i in r:
# 	x = factors(i)
# 	x.sort()
# 	x = x[1:len(x)-1]
# 	# print(str(i) + " " + str(x) )
# 	print(int(i/x[len(x)-1]) )