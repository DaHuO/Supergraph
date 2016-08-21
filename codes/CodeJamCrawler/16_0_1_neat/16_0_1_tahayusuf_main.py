def update_seen_digits(num, seen_digits):
    digits = get_digits(num)
    for d in digits:
        if d not in seen_digits:
            seen_digits.append(d)

    return [seen_digits, num]

def get_digits(n):

    digits = []
    while n:
        d = n % 10
        digits.append(d)
        n //= 10
    return digits

# reading
T = int(raw_input())
Y = []
for x in xrange(1, T + 1):
  for s in raw_input().split(" "):  # read a list of integers, 2 in this case
      n = int(s)
  Y.append(n)

# printing
x=1
for y in Y:

    seen_digits = []
    i=1
    isSlept = True
    while(isSlept):
        if y == 0:
            last_num = 'INSOMNIA'
            isSlept = False
        else:
            [seen_digits, last_num] = update_seen_digits(i * y, seen_digits)
            if len(seen_digits) == 10:
                isSlept = False
            i += 1

    print "Case #{}: {}".format(x, last_num)
    x += 1



