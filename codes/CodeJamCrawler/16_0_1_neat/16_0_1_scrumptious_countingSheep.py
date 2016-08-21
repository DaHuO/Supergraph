def count(number, digits):
    newly_seen = 0
    while number > 0:
        current_digit = number % 10
        if not digits[current_digit]:
            newly_seen += 1
            digits[current_digit] = True
        number //= 10
    return newly_seen

cases = int(input())
for case in range(cases):
    n = int(input())
    print('Case #', case+1, ': ', sep='', end='')
    if n == 0:
        print('INSOMNIA')
    else:
        digits = [False for x in range(10)]
        remaining = 10
        i = 1
        last = n
        while remaining > 0:
            last = n*i
            remaining -= count(last, digits)
            i += 1
        print(last)


