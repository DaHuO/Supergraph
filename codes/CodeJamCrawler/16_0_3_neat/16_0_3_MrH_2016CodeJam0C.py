# Open the given file 
lines = open("input.txt", "r").readlines()
t = int(lines[0].strip())
n, j = lines[1].split()
n = int(n.strip())
j = int(j.strip())

# The Big Idea is ...
def possible_coins(n):
    """Generates a list of possible jamcoins of length n"""
    coins = [[1]]
    for i in range(n-2):
        new_coins = []
        for coin in coins:
            new_coins.append(coin + [0])
            new_coins.append(coin + [1])
        coins = new_coins
    return [coin + [1] for coin in coins]

def nontrivial_divisor(n):
    """returns the lowest nontrivial divisor of n, or 0"""
    for i in range(2, int(n**(1/2)) + 1):
        if n%i == 0:
            return i
    return 0

def jamcoin(coin_as_list):
    """Returns a list of 9 nontrivial divisors, or []"""
    n = len(coin_as_list)
    list_of_divisors = []
    for base in range(2,10+1):
        in_base_10 = sum([coin_as_list[i]*base**(n-i-1) for i in range(n)])
        d = nontrivial_divisor(in_base_10)
        if d != 0:
            list_of_divisors.append(d)
        else:
            return []
    return list_of_divisors

coins_to_check = possible_coins(n)

# Create a file for the answer and ...
outfile = open("answer.txt", "w")
line1 = "Case #" + str(t) + ":" + "\n"
outfile.write(line1)
count = 0
for coin in coins_to_check:
    list_of_divisors = jamcoin(coin)
    if len(list_of_divisors) == 9:
        count = count + 1
        list_of_divisors = [str(i) for i in list_of_divisors]
        string_of_divisors = " ".join(list_of_divisors)
        coin = [str(i) for i in coin]
        coin_as_string = "".join(coin)
        line = coin_as_string + " " + string_of_divisors + "\n"
        outfile.write(line)
    if count == j:
        break
outfile.close()

