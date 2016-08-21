import math

def possibleCoins(coinLen, coinList, coin):
	if(coinLen == 0):
		coinList.append(coin)
		return
	else:
		possibleCoins(coinLen-1, coinList, coin)
		coin1 = coin[:]
		coin1[coinLen] = 0
		possibleCoins(coinLen-1, coinList, coin1)


def getForms(coin):
	forms = []
	for i in range(2, 11):
		number = 0
		coin.reverse()
		index = 0
		for digit in coin:
			if(int(digit) == 1):
				number += i**index
			index += 1
		forms.append(number)
		coin.reverse()
	return forms


def getDivisors(allForms):
	divs = []
	for form in allForms:
		for i in range(2,int(math.sqrt(form))):
			if(form%i == 0):
				divs.append(i)
				break
	return divs

def isJamCoin(divisors):
	if(len(divisors) == 9):
		return True
	else:
		return False



def giveJamCoins(coinLen, numCoins):
	coin = [1]*coinLen
	coinList = []
	jamCoins = []
	alldivs = []
	possibleCoins(coinLen-2, coinList, coin)
	for c in coinList:
		allForms = getForms(c)
		divisors = getDivisors(allForms)
		if(isJamCoin(divisors)):
			jamCoins.append(c)
			alldivs.append(divisors)
		if(len(jamCoins) == numCoins):
			break
	return (jamCoins, alldivs)


if __name__ == "__main__":
	lines = [line.rstrip('\n') for line in open('C-small-attempt0.in')]
	count = 0
	f = open('output.txt', 'w')
	for string in lines:
		if(count != 0):
			arr = string.split(' ')
			coinLen = int(arr[0])
			numCoins = int(arr[1])
			tup = giveJamCoins(coinLen, numCoins)
			f.write("Case #"+str(count)+": \n")
			i = 0
			for lst in tup[0]:
				f.write( (''.join([str(x) for x in lst])) + ' ' + ' '.join(map(str, (tup[1])[i])) + '\n') 
				i +=1
		count+=1