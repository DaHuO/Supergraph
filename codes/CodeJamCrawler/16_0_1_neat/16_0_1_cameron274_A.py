def run_test():
    n = int(raw_input())
    if (n == 0): return "INSOMNIA"
    not_seen = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    total = 0
    while(len(not_seen) != 0):
        total += n
        x = total
        while (x != 0):
            not_seen.discard(x%10)
            x //= 10
    return str(total)

t = int(raw_input())
for i in range(1, t+1):
    print("Case #%d: %s" % (i, run_test()))