def find_jamcoin(size, number):
    jamcoins = []
    x = 0
    comb = combinations(size-2)
    while(len(jamcoins) < number):
        coin = "1" + comb[x] + "1" 
        yas = base_conv(coin)
        if not has_prime(yas):
            divisors = find_divisors(yas)
            tup = coin, divisors
            jamcoins.append(tup)
        x+=1
    return jamcoins
def find_divisors(yas):
    d = []
    for x in range(0, len(yas)):
        for y in range(2, yas[x]):
            if(yas[x]%y == 0):
                d.append(y)
                break
    return d
def combinations(ta):
    comb = []
    for x in range(0, pow(2, ta)):
        use = bin(x)[2:len(bin(x))]
        if len(use) is not ta:
            zero = ""
            for x in range(0, ta-len(use)):
                zero += "0"
            use = zero+use
        comb.append(use)
    return comb
def base_conv(biy):
    bases = []
    for x in range(2, 11):
        number = 0
        place = 0
        for y in range(len(biy)-1, -1, -1):
            if(int(biy[y]) == 1):
                number += pow(x, int(place))
            place+=1
        bases.append(number)
    return bases

def has_prime(test):
    for x in range(0, len(test)):
        if(is_prime(test[x])):
            return True
    else:
        return False
def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True 
file_in = open(r"C:\Users\Isaac\Desktop\C-small-attempt0.in")
file_out = open(r"C:\Users\Isaac\Desktop\small_jamcoin.txt", mode="w")
numcases = file_in.readline()
case = (file_in.readline())
case = case[0: len(case)-1]
print(case)
length = distinct = ""
for x in range(0, len(case)):
    if(case[x] == " "):
        length = case[0:x]
        distinct = case[x:len(case)]
jamcoins = find_jamcoin(int(length), int(distinct))
file_out.write("Case #" + str(1) + ":\n")
for x in range(0, len(jamcoins)):
    file_out.write(jamcoins[x][0] + " ")
    for y in range(0, 9):
        file_out.write(str(jamcoins[x][1][y]) + " ")
    file_out.write("\n")
file_in.close()
file_out.close()
