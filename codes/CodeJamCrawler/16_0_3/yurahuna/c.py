def getProof(numbers):
    ret = []
    for number in numbers:
        is_divisor_found = False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                ret.append(i)
                is_divisor_found = True
                break
        if not is_divisor_found:
            return ret
    return ret


#############################

T = int(input())
N, J = map(int, input().split())

print("Case #1:")

for i in range(1<<(N-1), 1<<N):
    if i & 1 == 0:
        continue

    coin = [0] * N
    for j in range(N):
        coin[j] = (i >> j) & 1

    interpretations = []
    for base in range(2, 10 + 1):
        number = 0
        power = 1
        for j in range(N):
            number += coin[j] * power
            power *= base
        interpretations.append(number)

    divisors = getProof(interpretations)
    if len(divisors) == len(interpretations):
        print("".join(map(str, coin[::-1])), *divisors)
        J -= 1

    if J == 0:
        exit()
