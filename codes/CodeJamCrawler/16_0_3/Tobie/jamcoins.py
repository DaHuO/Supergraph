import math

length = 32
nb_coins = 500
nb_found = 0
print("Case #1:")

n = [1, 1, 1, 1, 1, 1, 1, 1, 1]
divisors = [1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(0, 9):
    n[i] = n[i] + (i + 2) ** (length - 1)
    
#############################################################
# Pre-computing: prime crible (hopefully as long as needed) #
#############################################################

limit = 10 ** 3
max_allowed_crible_length = int(math.sqrt(10 ** length)) + 1
if max_allowed_crible_length > limit:
    max_allowed_crible_length = limit

# Initializing crible
crible = []
for i in range(0, max_allowed_crible_length):
    crible.append(1)

primes = []
nb_primes = 0
# Computing crible itself
for i in range(0, max_allowed_crible_length):
    if crible[i] == 1:
        nb_primes += 1
        prime = i + 2
        primes.append(prime)
        #print(prime, "is prime.")
        for j in range(2 * prime, max_allowed_crible_length + 2, prime):
            crible[j - 2] = 0

crible = []

# Remove non-prime elements
nb_primes = len(primes)

max_prime = primes[len(primes) - 1]

######################
# Computing jamcoins #
######################

#while n[0] < 2 ** length:
while nb_found < nb_coins and n[0] < 2 ** length:
    nb_valid = 0

    for base in range(2, 11):
        if nb_valid == base - 2:
            root = int(math.sqrt(n[base - 2])) + 1

            for divisor in primes:
                if(divisor > root):
                    break
                if n[base - 2] % divisor == 0:
                    divisors[base - 2] = divisor
                    nb_valid = nb_valid + 1
                    break

            #for divisor in range(max_prime + 2, root):
                #if n[base - 2] % divisor == 0:
                    #divisors[base - 2] = divisor
                    #nb_valid = nb_valid + 1
                    #break

    if nb_valid == 9:
        print("{0:b}".format(n[0]), divisors[0], divisors[1], divisors[2], divisors[3], divisors[4], divisors[5], divisors[6], divisors[7], divisors[8])
        nb_found = nb_found + 1
        #for base in range(2, 11):
            #print("[DEBUG] Base=", base, " ", n[base - 2], " ", divisors[base - 2])
            
    n[0] = n[0] + 2
    binary = "{0:b}".format(n[0])
    for base in range(3, 11):
        n[base - 2] = int(binary, base)

#print("Total:", nb_found, "jamcoins")
