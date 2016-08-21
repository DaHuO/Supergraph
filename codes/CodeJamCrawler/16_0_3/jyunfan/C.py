
N = 32
J = 500

def get_a_divisor(n):
    if n < 4:
        return 0
    sqn = min(int(n**0.5), 100)
    for i in range(2, sqn+1):
        if n % i == 0:
            return i
    return 0

print('Case #1:')

n = 2**(N-1) + 1
count = 0
divisor = [0]*9
while count < J:
    satisfied = True
    str_n = bin(n)[2:]
#    print(str_n)
    for k in range(2,11):
        num_k = int(str_n, k)
#        print('base %d:%d' % (k, num_k))
        divisor[k-2] = get_a_divisor(num_k)
        if divisor[k-2] == 0:
            satisfied = False
            break
#        print('divisor: %d' % divisor[k-2])
    if satisfied:
        print('%s %s' % (str_n, ' '.join([str(x) for x in divisor])))
        count += 1

    n += 2
