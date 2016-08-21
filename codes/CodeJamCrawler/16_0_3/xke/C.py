import math

inputfile = open('C-large.in')
outputfile = open('C-large.out.txt', 'w')

# returns 0 if a prime number
# returns a divisor otherwise

# adaptation of
# https://www.daniweb.com/programming/software-development/code/216880/check-if-a-number-is-a-prime-number-python

def is_non_prime_get_divisor(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return False  
    # all other even numbers are not primes
    if not n & 1: 
        return 2
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return x
    return False


# intBase would be from 2 to 10, inclusive

def get_base_result(strCoin, intBase):
  
  return int(strCoin, intBase) # easy python way :) though below will work

  #lenCoin = len(strCoin)
  #listCoin = list(strCoin)
  #baseResult = 0
  #for i in range(lenCoin):
  #  baseResult = baseResult + (int(listCoin[lenCoin-1-i]) * (intBase ** i))
  #return baseResult


def is_jamcoin_get_proof(strCoin):

  lenCoin = len(strCoin)

  if len(strCoin) < 2:
    return False  # jamcoin too short

  listCoin = list(strCoin)
  if listCoin[0] != '1' or listCoin[lenCoin-1] != '1':
    return False # jamcoin not both 1's at end

  for i in range(lenCoin):
    if listCoin[i]!='1' and listCoin[i]!='0':
      return False

  # now, just need to check the prime-ness

  proofString = strCoin

  for b in range(2, 11): # 2 to 10 inclusive
    baseResult = get_base_result(strCoin, b)
    divisor = is_non_prime_get_divisor(baseResult)
    if divisor == False:
      return False # it's prime; non-jamcoin
    else:
      proofString = proofString + " " + str(divisor)

  return proofString







# Function for coming up w jamcoins. Criteria:
# - Every digit is either 0 or 1.
# - The first digit is 1 and the last digit is 1.
# - If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.


def output_jamcoins(N, J):


    #N = int length of Jamcoin string, >=2
    #J = int number of Jamcoins to print. Guaranteed to exist for N.

    # method: come up with variations of length N, and then see if it's a Jamcoin
    # variations must start w 1 and end with 1, which leaves N-2 variable chars

    variationChars = N-2
    numVariations = 2 ** (N-2)
    variationInt = 0  # this will turn into a string
    variationFormatter = "{0:0" + str(variationChars)+"b}"

    numJamcoins = 0
    strOutput = ""

    while numJamcoins < J:
      strCoin = "1" + variationFormatter.format(variationInt) + "1"
      
      #print strCoin
      #raw_input("Press Enter to continue...")

      variationInt = variationInt + 1 # keep varying until J jamcoins found!

      proof = is_jamcoin_get_proof(strCoin)

      if proof==False:
        #print "-"
        continue
      else:
        #print "-"
        strOutput = strOutput + proof + "\n"
        numJamcoins = numJamcoins + 1


    return strOutput





# --------------------------------------------


#skip first line
#next(inputfile)

#read first line:
num_cases = int(inputfile.readline())

for i in range(0, num_cases):
    
    line = inputfile.readline()

    # parse line: N J
    numbers = line.split()
    N = int(numbers[0]) 
    J = int(numbers[1]) 

    output_line = "Case #" + str(i+1) + ":\n" + output_jamcoins(N, J)
    print output_line
    outputfile.writelines(output_line)

inputfile.close()
outputfile.close()
