n = int(input())

def get_digits(n):
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    return digits

def count_sheep(t):
    if t == 0:
        return 'INSOMNIA'
    seen_digits = [0] * 10
    i = 1
    while(not all(seen_digits)):
        current_t = i * t
        d_in_ct = get_digits(current_t)
        for j in d_in_ct:
            seen_digits[j] = 1
        i += 1
    return current_t


for i in range(1, n + 1):
  t = int(input())
  print("Case #{}: {}".format(i, count_sheep(t)))
  # check out .format's specification for more formatting options
