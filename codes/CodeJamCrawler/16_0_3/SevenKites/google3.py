def prime(n):
    # a function that determines if a number n is a prime or not
    # returns True if prime, else false and also its lowest divisor
    is_prime = True
    divisor = 2
    root_of_n = int(n**(1/2))
    if n > 3:
        while divisor <= root_of_n and is_prime:
            if n % divisor == 0:
                is_prime = False
            if divisor > 2:
                divisor += 2
            else:
                divisor += 1
    if divisor == 3:
        divisor -= 1
    else:
        divisor -= 2
    return is_prime, divisor

#def digit_split(n):
    ## split up the digits of n
    ## 123 -> [3,2,1]
    #index = 1
    #digits = []
    #for iteration in range (len(str(n))):
        #num = (n // (index)) % 10
        #index *= 10
        #digits.append(num)
    #return digits

def digit_split(n):
    # split up the digits of n
    # 123 -> [3,2,1]
    str_n = str(n)
    digits = []
    for i in str_n:
        digits = [int(i)] + digits
    return digits

def base_calc(n, base):
    # returns the value of the number n in base base
    # 1011, 2 (base 2) -> 11
    digits = digit_split(n)
    value = 0
    for digit in range(len(digits)):
        if digits[digit] == 1:
            value += (base ** digit)
    return value

def is_jam_coins(n):
    # google problem: coin jam
    # returns True iff n is a jam coin
    base = 2
    are_prime = False
    value_list_divisor = []
    #if str(n)[0] == str(n)[-1] == '1':
    while base != 11 and not(are_prime):
        # value is the value of the number at base base
        value = base_calc(n,base)
        are_prime, divisor = prime(value)
        value_list_divisor.append(divisor)
        base += 1
    return_bool = not(are_prime), value_list_divisor
    #else:
        #return_bool = False, value_list
    return return_bool

def perm10(n):
    # input n, returns a set of all n length perms with any number of 1s or 0s
    if n == 0:
        return ['']
    elif n == 1:
        return ['0','1']
    else:
        lists = perm10(n-1)
        new_set = list()
        for i in lists:
            new_set.append('0' + i)
            new_set.append('1' + i)
        return new_set

def output(n, lines):
    # a number, lines lines of possible outputs
    new_list = list()
    # you only need to do n-2, because the first and last must be 1
    perms = perm10(n-2)
    for number in perms:
        new_list.append('1' + number + '1')
    return_output = ''
    line = 0
    element = 0
    length = len(new_list)
    while element != length and line != lines:
        value = new_list[element]
        boolean, lists = is_jam_coins(int(value))
        if boolean:
            return_output += value + ' ' + str(lists)[1:-1].replace(',','') + '\n'
            line += 1
        element += 1
    return return_output[:-1]

if __name__ == '__main__':
    file = open('C-small-attempt0.in.txt', 'r')
    line = 1
    case_number = 0
    for i in file:
        if line != 1:
            print('Case #' + str(case_number) + ':\n' + str(output(int(i[:2]),int(i[3:]))))
        else:
            line += 1
        case_number += 1