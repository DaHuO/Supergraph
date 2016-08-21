def helper(n,i, end):
    if i == end:
        yield n
    else:
        ln = list(n)
        ln[i] = "0"
        for r in helper("".join(ln), i+1, end):
            yield "".join(r)
        ln[i] = "1"
        for r in helper("".join(ln), i+1, end):
            yield "".join(r)
def generate_coins(N):
    n = N - 2
    begin = "".join("0" for i in range(n))
    for item in helper(begin, 0, n):
        yield "1" + item + "1"
