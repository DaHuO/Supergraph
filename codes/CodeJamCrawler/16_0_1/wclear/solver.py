def solve(n):
    if n == 0:
        return "INSOMNIA"
    else:
        notseen = list(range(0, 10))
        multiple = 1
        while (len(notseen) > 0):
            y = n * multiple
            parts = str(y)
            for char in parts:
                digit = int(char)
                if notseen.count(digit) > 0:
                    notseen.remove(digit)
            multiple += 1
        return "{}".format(y)