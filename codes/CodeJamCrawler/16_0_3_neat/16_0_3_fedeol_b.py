import math

def get_binToDec_range(n):
    a = '1' + '0'*(n-2) + '1'
    b = '1'*n
    
    return int(a, 2), int(b, 2)

def get_jamcoins(start_int, end_int, count):
    jamcoins = {}
    
    for coin in range(start_int, end_int + 1, 2):
        bin_str = bin(coin)[2:]
        factor_list = get_factor_list(bin_str)
    
        if factor_list is None:
            continue
        
        jamcoins[bin_str] = factor_list

        if len(jamcoins) == count:
            return jamcoins

    return None


def get_factor_list(binary):
    factor_list = []
    for base in range(2, 11):
        binary_int = int(binary, base)
        factor = get_factor(binary_int)
        
        if factor is None:
            return None

        factor_list.append(factor)

    return factor_list


def get_factor(value):
    for factor in range(2, int(math.sqrt(value)) + 1):
        if value % factor == 0:
            return factor
    return None

if __name__ == '__main__':
    input_data = open('C-small-attempt0.in').read().split('\n')
    n, j = tuple(map(int, input_data[1].split(' ')))
    
    """ a, b = range start and end """
    a, b = get_binToDec_range(n)
    
    jamcoins = get_jamcoins(a, b, j)
    jamcoins = [key + ' ' + ' '.join(map(str, value)) for key, value in jamcoins.items()]
    jamcoins = '\n'.join(jamcoins)
    
    with open('test.out', 'w') as out:
        out.write('Case #1:\n' + jamcoins);