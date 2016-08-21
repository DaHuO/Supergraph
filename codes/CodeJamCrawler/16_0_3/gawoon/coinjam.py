import math
import random

def is_prime(number):
    "from http://www.codeproject.com/Articles/691200/Primality-test-algorithms-Prime-test-The-fastest-w"
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0:
        return False
    
    oddPartOfNumber = number - 1
    
    timesTwoDividNumber = 0
    while oddPartOfNumber % 2 == 0:
        oddPartOfNumber = oddPartOfNumber / 2
        timesTwoDividNumber = timesTwoDividNumber + 1 

    for time in range(3):
        while True:
            randomNumber = random.randint(2, number)-1
            if randomNumber != 0 and randomNumber != 1:
                break
        
        randomNumberWithPower = pow(randomNumber, oddPartOfNumber, number)
        if (randomNumberWithPower != 1) and (randomNumberWithPower != number - 1):
            # number of iteration
            iterationNumber = 1
            
            while (iterationNumber <= timesTwoDividNumber - 1) and (randomNumberWithPower != number - 1):
                randomNumberWithPower = pow(randomNumberWithPower, 2, number)
                
                # inc the number of iteration
                iterationNumber = iterationNumber + 1
            if (randomNumberWithPower != (number - 1)):
                return False
    return True

def convert_base_n( jamcoin, base ):
    if base==10:
        return int(jamcoin)

    number = 0;
    while ( len(jamcoin) > 0 ):
        number += pow(base, len(jamcoin)-1) * int(jamcoin[0])
        jamcoin = jamcoin[1:]
    #print number
    return number

def is_jamcoin(jamcoin):
    if ( len(jamcoin) < 2 ):
        return False
    else:
        for base in range(2,11):
            number = convert_base_n(jamcoin, base)
            if is_prime( number ):
                return False
        return True

def generate_base2str(base10, LENGTH):
    str = "{0:b}".format(base10)
    while( len(str) < LENGTH ):
        str = '0' + str

    return '1' + str + '1'

def generate_jamcoin(N, J):
    answers = []
    for i in range(pow(N-2,2)):
        if len(answers) >= J:
            break

        generate = generate_base2str(i, N-2)
        if is_jamcoin( generate ):
            answers.append( generate )

    return answers

def get_nontrivial_divisor(jamcoin, base):
    i = convert_base_n(jamcoin, base)
    #i2 = convert_base_n(jamcoin, base+1)
    n = 2
    while True:
        if is_prime(n) and i % n == 0:# and (i2 % n) != 0:
            return n
        n = n+1
    return -1

def get_legitimate(jamcoin):
    proof = ""
    for base in range(2,11):
        proof += ' ' + str( get_nontrivial_divisor(jamcoin, base) )
    return proof

#print get_legitimate('1001')

#print is_prime(205891136943229)

#for i in range(10000):
#    print is_prime(205891136943229)

print is_prime(205891132094650)

f = open ( "./C-small-attempt2.in", 'r' )
foutput = open ( "./output.txt", 'w')

#f = open ( "./C-large.in", 'r' )
#foutput = open ( "./output_large.txt", 'w')
T = int(f.readline())
if T >= 1 and T <= 100:
    i = 1
    while True:
        input = f.readline()
        if not input:
            break

        inputs = input.split(' ')
        N = int(inputs[0])
        J = int(inputs[1])

        print N
        print J

        output = 'Case #'+ str(i) + ':\n'
        foutput.write(output)

        answers = generate_jamcoin(16, 50)
        for answer in answers:
            output = answer + get_legitimate(answer)
            foutput.write(output + '\n')
        i = i+1
else:
    print('Limits Invalid')

f.close()
foutput.close()
