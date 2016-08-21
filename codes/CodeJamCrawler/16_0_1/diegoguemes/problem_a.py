def digits_for_number(number):
    return set([digit for digit in str(number)])

def last_number_before_seeing_all_digits(N):
    if N == 0:
        return 'INSOMNIA'
    i = 0
    digits = set()
    while len(digits) < 10:
        i += 1
        digits = digits.union(digits_for_number(i * N))
    return i * N

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    print('Case #{}: {}'.format(t, last_number_before_seeing_all_digits(N)))

