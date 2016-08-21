import math

def get_divisors(number):
    some_list = []
    upto = int(math.sqrt(number))+1
    for i in range(2,upto):
        if number % i == 0:
            number /= i
            some_list.append(i)
        while number % i == 0:
            number /= i
    return some_list

# using the get divisor method the prime divisors for (1 + n^ 15) are for n in [2:10]:
N16_divisors = {2: [3, 11], 3: [2, 7, 31, 61], 4: [5, 13, 41, 61], 5: [2, 3, 7, 61], 6: [7, 11, 31, 101], 7: [2, 11, 43, 191],
8: [3, 11, 19, 331], 9: [2, 5, 73, 1181], 10: [7, 11, 13, 211, 241, 2161]}
N16_max = 16384

# using the get divisor method the prime divisors for (1 + n^31) are for n in [2:10]:
N32_divisors = {2: [3], 3: [2], 4: [5, 5581, 8681], 5: [2, 3, 1303], 6: [7], 7: [2, 373], 8: [3], 9: [2, 5], 10: [11]}
N32_max = 1073741824
N32_max = 107374

def check_divisibility(num, base, divisor):
    base10 = convert_to_base10(num, base)
    if base10 % divisor == 0:
        return True
    else:
        return False

def convert_to_base10(num, base):
    digits = map(int, list(str(num)))
    base10 = 0
    for i in range(len(digits)):
        base10 += (base ** (len(digits) - i - 1)) * digits[i]
    return base10

def convert_to_base2(num):
    some_list = []
    while num / 2 > 0:
        some_list.append(num%2)
        num /= 2
    some_list.reverse()
    return ''.join(map(str, some_list))
        
def formatted_output(num_list):
    for i in num_list.keys():
        result = str(i) + ' ' + ' '.join(map(str, num_list[i]))
        print result
        #test_result(result)

def finalize_coin(str, N):
    missing = '0' * (N-2-len(str))
    return '1' + missing + str + '1'

def make_numbers(N,J):
    if N == 16:
        maxx = N16_max
        divs = N16_divisors
    elif N == 32:
        maxx = N32_max
        divs = N32_divisors
    num_list = {}
    for i in range(1,maxx):
        candidate = convert_to_base2(i) + '0'
        temp_list = []
        for base in range(2,11):
            for div in divs[base]:
                if check_divisibility(candidate, base, div):
                    temp_list.append(div)
                    break
            if len(temp_list) < base - 1:
                break
        if len(temp_list) == 9:
            num_list[finalize_coin(convert_to_base2(i), N)] = temp_list
        if len(num_list) >= J:
            break
    return num_list

def test_result(str):
    nums = str.split(' ')
    for i in range(2,11):
        print convert_to_base10(nums[0], i) % int(nums[i-1])

t = int(raw_input())
for i in range(1, t + 1):
    N, J = [int(s) for s in raw_input().split(" ")]
print 'Case #1:'
formatted_output(make_numbers(N, J))