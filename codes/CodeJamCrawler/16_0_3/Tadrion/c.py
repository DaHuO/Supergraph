import random
import math

#http://www.codeproject.com/Articles/691200/Primality-test-algorithms-Prime-test-The-fastest-w
def MillerRabinPrimalityTest(number):
    '''
    because the algorithm input is ODD number than if we get
    even and it is the number 2 we return TRUE ( spcial case )
    if we get the number 1 we return false and any other even 
    number we will return false.
    '''
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0:
        return False
    
    ''' first we want to express n as : 2^s * r ( were r is odd ) '''
    
    ''' the odd part of the number '''
    oddPartOfNumber = number - 1
    
    ''' The number of time that the number is divided by two '''
    timesTwoDividNumber = 0
    
    ''' while r is even divid by 2 to find the odd part '''
    while oddPartOfNumber % 2 == 0:
        oddPartOfNumber = oddPartOfNumber / 2
        timesTwoDividNumber = timesTwoDividNumber + 1 
     
    '''
    since there are number that are cases of "strong liar" we 
    need to check more then one number
    '''
    for time in range(6):
        
        ''' choose "Good" random number '''
        while True:
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            if randomNumber != 0 and randomNumber != 1:
                break
        
        ''' randomNumberWithPower = randomNumber^oddPartOfNumber mod number '''
        randomNumberWithPower = pow(randomNumber, oddPartOfNumber, number)
        
        ''' if random number is not 1 and not -1 ( in mod n ) '''
        if (randomNumberWithPower != 1) and (randomNumberWithPower != number - 1):
            # number of iteration
            iterationNumber = 1
            
            ''' while we can squre the number and the squered number is not -1 mod number'''
            while (iterationNumber <= timesTwoDividNumber - 1) and (randomNumberWithPower != number - 1):
                ''' squre the number '''
                randomNumberWithPower = pow(randomNumberWithPower, 2, number)
                
                # inc the number of iteration
                iterationNumber = iterationNumber + 1
            '''     
            if x != -1 mod number then it because we did not found strong witnesses
            hence 1 have more then two roots in mod n ==>
            n is composite ==> return false for primality
            '''
            if (randomNumberWithPower != (number - 1)):
                return False
            
    ''' well the number pass the tests ==> it is probably prime ==> return true for primality '''
    return True 

#http://stackoverflow.com/questions/2267362/convert-integer-to-a-string-in-a-given-numeric-base-in-python
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]
	
	
N = 16
J = 50
r = 0
lim = 10000000000

res = []
dotychczas = []
while (r < J):
	s = [1]
	for i in xrange(N-2):
		s.append(random.randint(0,1))
	s.append(1)
	
	dd = []
	ok = 1
	for base in range(2,11):
		c = 0
		for i in range(N):
			c = base*c + s[i]
		if MillerRabinPrimalityTest(c):
			ok = 0
			break
		else:
			dd.append(c)
	
	if ok and (dd[8] not in dotychczas):
		#print dd[8]
		ee = []
		cnt1 = 0
		for z in dd:
			while True:
				dziel = random.randint(2,int(math.ceil(math.sqrt(z))))
				cnt1 = cnt1 + 1
				if z % dziel == 0:
					ee.append(dziel)
					break
				if cnt1 > lim:
					break
			if cnt1 > lim:
				break
		
		if cnt1 <= lim:
			dotychczas.append(dd[8])
			print dd[8],
			for y in ee:
				print y,
			print 
			r = r+1
	