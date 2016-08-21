def function(N):
    symbol = N[0]
    result = 0

    for ele in list(N):
        if symbol == ele:
            continue
        else:
            symbol = ele
            result += 1

    if symbol == '+':
        return result
    else:
        return result + 1


if __name__ == '__main__':
    with open('A-small-attempt0.in') as fin:
        T = int(fin.readline())
        for _ in range(T):
            N = fin.readline()[:-1]  # get input
            out = function(N)
            with open('out.txt', 'a') as fout:
                fout.write('Case #%d: %s\n' % (_ + 1, out))
