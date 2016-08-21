from math import pow
from multiprocessing import Pool

numbers = {}

def check_prime(num):
    try:
        return numbers[num]
    except KeyError:
        pass

    if num > 1:
        for i in range(2,int(pow(num, 0.5)+1)):
            if (num % i) == 0:
                numbers[num] = [0,i]
                [numbers.update({num*j: [0,i*j]}) for j in range(2,1000)]
                try:
                    numbers[pow(2,num)-1] = [0,i]
                except:
                    pass
                return 0,i
    else:
        numbers[num] = [0,0]
        return 0,0
    numbers[num] = [1,None]
    return 1,None

def change_base(num, base):
    number = sum([pow(base, i)*int(cr) for i,cr in enumerate(num[::-1])])
    return int(number)

def get_str(length):
    min_val = pow(2, length-1)+1
    return int(min_val)

def get_prime_numbers(N):
    min_val = get_str(N)
    max_val = change_base([1 for i in range(N+1)], 2)
    for val in range(min_val, max_val+1):
        if check_prime(val) == 1:
            yield val
    yield -1

def check_prime_base_comb(base_num):
    base,num = base_num
    check,factor = check_prime(change_base(num,base))
    return base,factor
p = Pool(4)

def get_coinjam(N, limit):
    found = 0
    for i in range(int(pow(2, N-2))):
        num  = ['1'] + [str(int(int(i/pow(2,j-1))%2)) for j in range(N-2, 0, -1)] + ['1']
        #print(num)
        #print([change_base(num,base) for base in range(2,11)])
        #primes = [check_prime(change_base(num,base))[1] for base in range(2,11)]
        all_good = True
        denoms = []

        for ranges in [(2,7), (7,11)]:
            base_num_comb = [(base,num) for base in range(ranges[0],ranges[1])]
            output = p.map(check_prime_base_comb, base_num_comb)
            output = sorted(output, key=lambda item: item[0])
            for base,factor in output:
                if not factor:
                    all_good = False
                    break
                denoms.append(str(factor))
            if not all_good:
                break

        if all_good:
            print("".join(num), " ".join(denoms))
            found += 1

        if found >= limit:
            break

count = int(input())
for i in range(count):
    n,j = input().split()
    n = int(n)
    j = int(j)
    print("Case #%s:" % str(i+1))
    get_coinjam(n,j)
