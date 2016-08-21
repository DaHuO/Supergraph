__author__ = 'Kholofelo Moyaba'


def update_seen(counted, d):
    while d > 0:
        counted[d % 10] = True
        d /= 10

    num_true = 0
    for b in counted:
        num_true += 1 if b else 0

    return num_true


def count(n):
    counted = [False, False, False, False, False, False, False, False, False, False]
    start_n = n
    if n < 1:
        return 'INSOMNIA'
    i = 0
    while True:
        num_seen = update_seen(counted, n)
        if num_seen == 10:
            return str(n)
        n += start_n
        i += 1
    # no need for stop case: unless for resources reasons (don't want program to run too long)
    # (for N>0, you can also find an i, such that N*i has whatever digit you want

# ==================================
# Start
cases = int(raw_input())
case = 1
while cases >= case:
    start = int(raw_input())
    print("Case #%s: %s" % (str(case), count(start)))
    case += 1