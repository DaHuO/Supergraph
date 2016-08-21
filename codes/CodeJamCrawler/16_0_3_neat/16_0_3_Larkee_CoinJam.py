import math

def coin_jam(filename):
    file = open(filename,'r')
    source = file.read()
    file.close()
    lines = source.splitlines()
    T = int(lines[0])
    N = int(lines[1].split()[0])
    J = int(lines[1].split()[1])
    file = open("game_jam.out", 'w')
    for i in range(T):
        file.write("Case #" + str(i+1) + ":\n")
        strings = generate_strings(N, J)
        for string in strings:
            file.write(string + return_proof(string) + '\n')
    file.close()

def convert_to_base(string, base):
    decimal_number = 0
    for i in range(-1, -len(string)-1, -1):
        if string[i] == '1':
          decimal_number += pow(base, abs(i)-1)
    return decimal_number

def is_prime(number):
    if divisible_by(number) < 0:
      return True
    return False

def divisible_by(number):
    for i in range(2, int(math.sqrt(number)+1)):
        if number%i == 0:
            return i
    return -1

def is_coin_jam(string):
    for char in string:
        if char is not '1' and char is not '0':
            return False
    if string[0] is not '1' or string[-1] is not '1':
        return False
    for i in range(2, 11):
        number = convert_to_base(string, i)
        if is_prime(number):
            return False
    return True

def return_proof(string):
    output = ''
    for i in range(2, 11):
        number = convert_to_base(string, i)
        output += ' ' + str(divisible_by(number))
    return output

def generate_strings(length, limit):
    strings = []
    generated = 0
    for i in range(2**(length-1)+1, 2**length, 2):
        string = bin(i)[2:]
        if is_coin_jam(string):
            strings += [string]
            generated += 1
            if generated == limit:
                return strings


coin_jam("C-small-attempt0.in")
