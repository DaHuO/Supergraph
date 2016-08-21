def count_sheep(n):
    if n == 0:
        return "INSOMNIA"
    counter = 1
    current = n
    result = set()
    while counter < 1000:
        current = n * counter
        result=result.union(set(list(str(current))))
        if len(result) == 10:
            return current
        else:
            counter += 1
    return "INSOMNIA"


t = int(input())
for i in range(t):
    n = int(input())
    print("Case #%d: %s" % (i+1, count_sheep(n)))


