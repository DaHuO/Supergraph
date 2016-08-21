from sys import argv


# prime numbers files from https://www.mathsisfun.com/numbers/prime-number-lists.html
# from 1 to 1M
prime_list = []
prime_list.append(1)
for x in range(1, 11):
    f = open('primes-to-' + str(x) + '00k.txt', 'r')
    for i in f:
        prime_list.append(long(i))
    
    
def find_div(n):
    """ Returns the divisible number if n is not prime, else -1 """
    for d in prime_list[1:]:
        if d > n**0.5:
            return -1
        if not (n % d):
            return d

   
def get_first_candidate(n):
    """ return the 1st candidate 10000001 type. with n-2 times of '0' """
    return '1' + '0' * (n - 2) + '1'
    
def get_next_candidate(current):
    """ Return the next jamcoin candidate
        n (str)
    """
    s = bin(long(current[1:-1], 2) + 1)[2:]
    if len(s) > len(current):
        return ''
    return '1' + '0' * (len(current) - len(s) - 2) + s + '1'
    
    
def base_list(n):
    """ Generates the list of base 2 to 10 interpretation of the number n 
        n (str)
    """
    return [long(n, x) for x in range(2, 11)]
    
def is_jamcoin(n):
    divs = []
    for x in base_list(n):
        tmp = find_div(x)
        if tmp == -1:
            return (False, [])
        divs.append(tmp)
    return (True, divs)
    
    
def main():
    script, filename = argv
    in_file = open(filename, 'r')
    out_file = open(filename.split('.')[0] + '.out', 'w')
    list = []
    num = 0
    try:
        for i, line in enumerate(in_file):
            print(line)
            if not i: num = int(line.strip())
            else : list.append(line.strip().split(' '))
    except:
        pass
    in_file.close()
    
    for x in range(num):
        N = int(list[x][0])
        J = int(list[x][1])
        candidate = get_first_candidate(N)
        count = 1
        print('Case #' + str(x + 1) + ':')
        out_file.write('Case #' + str(x + 1) + ':')
        while count <= J:
            tf, divs = is_jamcoin(candidate)
            if tf and None not in divs:
                #print(str(long(bin(n)[2:])) + ' ' + str(divs))
                out_file.write('\n' + candidate)
                for i in divs:
                    out_file.write(' ' + str(i))
                count += 1
            candidate = get_next_candidate(candidate)            
    out_file.close()

if __name__ == '__main__':
    main()