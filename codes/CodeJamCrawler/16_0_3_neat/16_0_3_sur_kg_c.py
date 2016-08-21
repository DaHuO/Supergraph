
print('Case #1:')

coin_len = 32
coin_cnt = 500
prim_max = 100000;


start_s = '1' * coin_len
finish_s = '1' + '0' * (coin_len - 2) + '1'
start_n = int(start_s, 2)
finish_n = int(finish_s, 2)

primes = []
erat = [1] * prim_max
for i in range(2, prim_max):
    if erat[i]:
        primes.append(i)
        for j in range(i * 2, prim_max, i):
            erat[j] = 0


found = 0
current = start_n
while current >= finish_n:
    curr_s = format(current, 'b')
    divisors = [None] * (10+1)
    for base in range(2, 10+1):
        curr_n = int(curr_s, base)
        #print(base, curr_n, end = '\n')
        if curr_n < prim_max and erat[curr_n]:
            break
        for d in primes:
            if curr_n % d == 0:
                divisors[base] = d
                break
        else:
            break
    else:
        found = found + 1
        #print('%d of %d found:' % (found, coin_cnt))
        print(curr_s, end = ' ')
        print(*divisors[2:10+1], sep = ' ', end = "\n")
    current = current - 2
    if found == coin_cnt:
        break
else:
    print('%d of %d found' % (found, coin_cnt))
    pass

