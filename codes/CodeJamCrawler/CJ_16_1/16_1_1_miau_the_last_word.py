
def main():
    cases = int(input())
    for case in range(cases):
        (s,) = input().split()
        result = solve(s)
        print("Case #%d: %s" % (case + 1, result))

def solve(s):
    result = []
    for c in list(s):
        if len(result) == 0:
            result.append(c)
            continue
        for c2 in result:
            if c2 < c:
                result[0:0] = c
                break
            elif c2 > c:
                result.append(c)
                break
        else:
            result.append(c)

    return "".join(result)

main()
