N = 16
J = 50

# returns divisor, or false if n is prime
def get_divisor(n):
    if n == 2 or n == 3: return False
    if n%2 == 0: return 2
    if n < 9: return False
    if n%3 == 0: return 3
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return f
        if n%(f+2) == 0: return f+2
        f +=6
    return False

found = {}
num_found = 0

print "Case #1:"

size = N - 2
i = 0
while num_found < 50:
    number = str(bin(i))[2:].zfill(size)
    potential_coin = "1" + number + "1"
    numerical_values = [int(potential_coin, base) for base in range(2,11)]
    if all([get_divisor(v) for v in numerical_values]):
        print potential_coin, ' '.join([str(get_divisor(v)) for v in numerical_values])
        found[potential_coin] = [get_divisor(v) for v in numerical_values]
        num_found += 1
    i += 1

