import math

def is_prime(x):
    i = 2.0
    sqrtx = math.sqrt(x)
    while i < sqrtx:
        if int(x / i) == x / i:
            return int(i)
        i = i + 1
    return -1

def find_jamcoins(length, how_many):
    changing = ("0" * (length - 2))
    jamcoin = "1"+changing+"1"
    coins = []
    while len(coins) < how_many: 
        factors = []
        for i in [2,3,4,5,6,7,8,9,10]:
            factor = is_prime(int(jamcoin, i))
            if factor == -1:
                break
            else:
                factors.append(factor)
        if len(factors) == 9:
            coins.append((jamcoin, factors))
        changing = bin(int(changing, 2) + 1)[2:]
        while len(changing) < (length - 2):
            changing = "0" + changing 
        jamcoin = "1"+changing+"1"
    return coins
        

def solve_N(string):
    output = ""
    args = string.split(" ")
    N = int(args[0])
    J = int(args[1])
    coins = find_jamcoins(N, J)
    for coin in coins:
        output = output + "\n" + coin[0] + " "+ " ".join(map(lambda x: str(x), coin[1]))
    return output

def solve(Ns):
    for i in range(len(Ns)):
        print "Case #"+str(i+1)+": "+solve_N(Ns[i])

def parse(filename):
    f = open(filename)
    lines = f.readlines()
    num_inputs = int(lines[0])
    inputs = []
    for x in range(num_inputs):
        inputs.append(lines[x+1].strip())
    solve(inputs)

parse("C-small-attempt0.in")
