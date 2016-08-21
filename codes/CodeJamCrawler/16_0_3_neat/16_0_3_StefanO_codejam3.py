def getFactor(n):    
    for i in range(3, 20): 
        if(n % i == 0):
            return i
    return 0

def coinIsJam(coin):
	for j in range(2,11):
		if(isPrime(int(coin,j))):
			return False
	return True

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  x = 0
  while f <= r and x < 100:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    x += 1
    f +=6
  return True 

f = open('output.txt','w')
f.write('Case #1:\n')
answer = 0;
for i in range(0,16384):
	coin = '1'+ '{:014b}'.format(i) + '1'
	if(coinIsJam(coin)):
		coin2 = getFactor(int(coin,2))
		coin3 = getFactor(int(coin,3))
		coin4 = getFactor(int(coin,4))
		coin5 = getFactor(int(coin,5))
		coin6 = getFactor(int(coin,6))
		coin7 = getFactor(int(coin,7))
		coin8 = getFactor(int(coin,8))
		coin9 = getFactor(int(coin,9))
		coin10 = getFactor(int(coin,10))
		if(coin2 != 0 and coin3 != 0 and coin4 != 0 and coin5 != 0 and coin6 != 0 and coin7 != 0 and coin8 != 0 and coin9 != 0 and coin10 != 0):
			#print(str(int(coin,2)),str(int(coin,3)),str(int(coin,3)),str(int(coin,4)), str(int(coin,4)), str(int(coin,6)), str(int(coin,7)), str(int(coin,8)), str(int(coin,3)), str(int(coin,10)))			
			string = str(int(coin,10)) + ' ' + str(coin2) + ' ' + str(coin3) + ' ' + str(coin4) + ' ' + str(coin5) + ' ' + str(coin6) + ' ' + str(coin7) + ' ' + str(coin8) + ' ' + str(coin9) + ' ' + str(coin10) + ' ' + '\n'
			f.write(string)
			answer += 1
			if(answer == 50):
				break
