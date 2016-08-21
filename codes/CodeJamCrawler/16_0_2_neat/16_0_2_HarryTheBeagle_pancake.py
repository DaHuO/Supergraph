def pancake(s):
    i = 0
    result = 0
    prev = None
    while i < len(s):
        if prev is None or prev == s[i]:
            prev = s[i]
        else:
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
            if prev == "+":
                result += 2
            else:
                result += 1
            prev = "+"
        i += 1
    if prev == "-":
        result += 1

    return result


    """
    start = 0
    result = 0
    for i in xrange(len(s)):
        if s[i] == "-":
            if i == len(s) - 1 or s[i + 1] == "+":
                # start .. i-1 are happy
                if start > -1 and i - start > 0:
                    result += 2
                else:
                    result += 1
                start = i + 1
        elif start == -1:
            start = i
    return result
    """





if __name__ == "__main__":
        T = int(raw_input())
        for i in xrange(1, T + 1):
            s = raw_input()
            print "Case #{}: {}".format(i, pancake(s))
