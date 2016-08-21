import sys
from itertools import product

def get_int(data, base):
    reversed_data = data[::-1]
    total = 0
    for index, digit in enumerate(reversed_data):
        if digit != 0:
            total += digit * (base**index)
    return total

prime_proof_dict = {}

def prove_not_prime(n):
    if n in prime_proof_dict:
        return prime_proof_dict[n]
    for div in range(2, n-1):
        if div**2 > n:
            break
        if n % div == 0:
            prime_proof_dict[n] = div
            return div
    prime_proof_dict[n] = -1
    return -1

def prove_jam_coin(data):
    proof = []
    for i in range(2,11):
        number = get_int(data, i)
        divisor = prove_not_prime(number)
        if divisor == -1:
            return False
        proof.append(divisor)
    return proof

n = 16
j = 50
print("Case #1:")
for number_digits in product([0,1], repeat=n-2):
    data = [1] + list(number_digits) + [1]
    proof = prove_jam_coin(data)
    if proof:
        string = ''.join([str(x) for x in data])
        proof_string = ' '.join([str(x) for x in proof])
        print(string, proof_string)
        j -= 1
        if j == 0:
            break
