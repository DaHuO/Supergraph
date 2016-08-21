def flipover(s):
    string = ''
    for x in s[::-1]:
        if x == '+':
            string += '-'
        else:
            string += '+'
    return string

def cleanTail(s):
    if len(s) == 0 or s.count('+') == len(s):
        return ''
    index = len(s) - 1
    while s[index] == '+':
        index -= 1
    return s[:index + 1]


def maneuver(s, cnt):
    if len(s) > 0 and s.count('+') == len(s):
        return cnt
    if len(s) > 0 and s.count('-') == len(s):
        return cnt + 1
    if len(s) == 0 or len(s) == 1:
        if s == '-':
            cnt += 1
        return cnt
    if len(s) == 2:
        if s == "-+" or s == "--":
            cnt += 1
        elif s == "+-":
            cnt += 2
        return cnt

    # general cases
    if s[0] == '-' and s[-1] == '-':
        cnt += 1
        return maneuver(cleanTail(flipover(s)), cnt)
    elif s[0] == '+' and s[-1] == '-':
        index = 0
        while s[index] == '+':
            if index == len(s) - 1:
                break
            index += 1
        cnt += 1
        str_in = flipover(s[:index]) + s[index:]
        return maneuver(cleanTail(str_in), cnt)
    elif s[0] == '-' and s[-1] == '+':
        index = 0
        while s[index] == '-':
            if index == len(s) - 1:
                break
            index += 1
        cnt += 1
        str_in = s[index:] + flipover(s[:index])
        return maneuver(cleanTail((str_in)), cnt)
    else:
        index = 0
        while s[index] == '+':
            if index == len(s) - 1:
                break
            index += 1
        cnt += 1
        str_in = flipover(s[:index]) + s[index:]
        return maneuver(cleanTail(str_in), cnt)


t = int(raw_input())
for i in xrange(1, t + 1):
    pancakes = raw_input()
    res = maneuver(pancakes, 0)
    print "Case #{}: {}".format(i, maneuver(pancakes, 0))
