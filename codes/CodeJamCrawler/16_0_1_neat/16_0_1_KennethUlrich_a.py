import fileinput

for e, line in enumerate(fileinput.input()):
    if fileinput.isfirstline():
        continue
    v = int(line.strip())
    if v == 0:
        result = "INSOMNIA"
    else:
        required = set(range(10))
        result = 0
        while required:
            result += v
            q = result
            while q:
                q, r = divmod(q, 10)
                required.discard(r)
    print "Case #{}: {}".format(e, result)
