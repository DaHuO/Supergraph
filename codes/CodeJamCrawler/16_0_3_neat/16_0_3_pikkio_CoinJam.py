import random

N = 32
J = 500

# ugh! brute force... but I'm running out of time...
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if (i > 100000):
            break
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
            break
    if n > 1:
        factors.append(n)
    return factors


output_file = open("results.txt", "w+")
output_file.write("Case #1:\n")

jamcoins = [ ]

for i in range(J):
    jamcoin_added = False
    while (not jamcoin_added):
        
        jamcoin_generated = False
        while (not jamcoin_generated):
            number = pow(10, N-1) + 1
            
            for j in range(1, N-2):
                number += random.randint(0, 1) * pow(10, j)
            
            if not (number in jamcoins):
                jamcoin_generated = True
        
        jamcoin_checked = True
        factors_str = ""
        number_str = str(number)
        for b in range(2, 11):
            pf = prime_factors(int(number_str, b))
            
            if (len(pf) == 1):
                jamcoin_checked = False
                break
            
            factors_str += str(pf[0]) + " "
        
        if (jamcoin_checked):
            jamcoins.append(number)
            jamcoin_added = True
            output_file.write(number_str + " " + factors_str + "\n")
            print(number)

output_file.close()