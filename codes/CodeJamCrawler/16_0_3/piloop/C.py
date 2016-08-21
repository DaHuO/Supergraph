MAX_NUM = 2 ** 22
isPrime = [None] * (MAX_NUM + 1)
primes = []
for i in range(2, MAX_NUM):
    if isPrime[i] is not None:
        continue
    primes.append(i)
    for j in range(2 * i, MAX_NUM, i):
        if isPrime[j] is None:
            isPrime[j] = i

with open('C-small.in') as input:
    with open('C-small-ans.txt', 'w') as out:
        tests = input.readline()
        n, cnt = input.readline().split()
        n = int(n)
        cnt = int(cnt)
        for i in xrange(2 ** (n - 2)):
            if cnt == 0:
                break
            arr = [1]
            for j in range(n - 2):
                if (i & (1 << j)) != 0:
                    arr.append(1)
                else:
                    arr.append(0)
            arr.append(1)
            arrStr = "".join(map(lambda s: str(s), arr))
            good = True
            ans = []
            for base in range(2, 11):
                num = 0L
                for j in range(n):
                    num += arr[j] * (base ** j)
                if num < MAX_NUM:
                    if isPrime[num] is None:
                        good = False
                        break
                    else:
                        ans.append(isPrime[num])
                else:
                    any_p = -1
                    for p in primes:
                        if num % p == 0:
                            any_p = p
                            break
                    if any_p == -1:
                        good = False
                        break
                    else:
                        ans.append(any_p)

            if good:
                cnt -= 1
                print(arrStr[::-1] + ' ' + ' '.join(map(lambda s: str(s), ans)))
