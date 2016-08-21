def all_digits_found(found):
    all_digits = [str(x) for x in range(10)]
    found_digits = [x for x in found]
    if sorted(all_digits) == sorted(found_digits):
        return True
    return False

def counting(number):
    digits_found = list(set([x for x in str(number)]))
    N = number
    if number == 0:
        return 'INSOMNIA'
    i = 1
    while not all_digits_found(digits_found):
        i += 1
        number = i * N
        num_digits = list(set([x for x in str(number) if x not in digits_found]))
        digits_found = digits_found + num_digits
    return number

i = 0
for test in range(int(raw_input().strip())):
    N = int(raw_input().strip())
    i += 1
    print 'Case #{}: {}'.format(i, counting(N))