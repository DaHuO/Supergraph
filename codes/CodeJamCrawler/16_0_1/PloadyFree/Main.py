def check(n):
    if n == 0:
        return -1
    used = [False] * 10
    used_count = 0
    for k in range(1, 10000 + 1):
        cur_n = n * k
        while cur_n > 0:
            digit = cur_n % 10
            if not used[digit]:
                used[digit] = True
                used_count += 1
            cur_n //= 10
        if used_count == 10:
            return n * k
    return -1


t = int(input())
for case_number in range(1, t + 1):
    result = check(int(input()))
    if result == -1:
        result = 'INSOMNIA'
    print('Case #%d: %s' % (case_number, result))
