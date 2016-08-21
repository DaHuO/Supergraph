import itertools

def is_prime(n):
    n = int(n)
    if n < 2:
         return False;
    if n % 2 == 0:
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def base_to_10(num_str, base):
    num_list = []
    while int(num_str) > 0:
        num_list.append(int(num_str) % 10)
        num_str = int(num_str) // 10
    dec_num = 0
    power = 0
    for i in num_list:
        dec_num = dec_num + (int(i))*(base**power)
        power += 1
    return dec_num

def get_divisor(num):
    num = int(num)
    for x in range(2, num):
        if num % x == 0:
            return x

# supporting method for is_jamcoin and jamcoin_and_divisor
def get_bases(jamcoin):
    all_bases = []
    for x in range(2, 11):
        all_bases.append(base_to_10(jamcoin, x))
    return all_bases

def is_jamcoin(jamcoin):
    all_bases = get_bases(jamcoin)
    for each in all_bases:
        if is_prime(each) is True:
            return False
    return True

def jamcoin_and_divisor(jamcoin):
    bases_array = get_bases(jamcoin)
    divisors = []
    for each in bases_array:
        divisors.append(get_divisor(each))
    return divisors

# main

ip = open("C-small-attempt0.in", "r")
op = open("output.txt", "w")
num_cases = ip.readline()
N_J = ip.readline()
N_J = [int(x) for x in N_J.split(' ')]
N = N_J[0]
J = N_J[1]

to_permute = ['0', '1']
results = list(itertools.product(to_permute, repeat=N-2))

jamcoins = []

for result in results:
    result = '1'+''.join(result)+'1'
    if len(jamcoins) == J:
        break
    elif is_jamcoin(result) is False:
        pass
    else:
        jamcoins.append([result, jamcoin_and_divisor(result)])

op.write("Case #1:\n")
for x in range(len(jamcoins)):
    op.write(jamcoins[x][0] + ' ' +  ' '.join(str(y) for y in jamcoins[x][1]) + '\n')
print("done")
ip.close()
op.close()
