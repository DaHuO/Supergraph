import pyprimesieve
# Library from here: https://pypi.python.org/pypi/pyprimesieve

first_number = "1"+"0"*30+"1"
last_number =  "1"+"1"*30+"1"
first_thousand_primes = pyprimesieve.primes(5000)

def is_prime_in_base(num_str, base):
    n = int(num_str, base=base)
    for i in first_thousand_primes:
        if n %i ==0: return i
    return -1

print "Case #1:"
J = 0
current_number = first_number
while J!=500:
    factors = []
    correct = True
    for base in xrange(2,10+1): # for each base
        factor = is_prime_in_base(current_number, base)
        if factor != -1:
            factors.append(factor)
        else:
            correct = False
            break
    if correct:
        print current_number,
        for factor in factors: print factor,
        print ""
        J+=1
    current_number = bin(int(current_number, 2) + 2)[2:]

