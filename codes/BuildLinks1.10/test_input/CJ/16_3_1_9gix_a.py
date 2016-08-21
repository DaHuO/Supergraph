import collections

def evac_plan(s):
    data = collections.Counter(s)
    _ = ""
    length = sum(data.values())
    while length > 0:
        result = data.most_common(2)
        data.subtract(result[0][0])
        _ += result[0][0]
        length -= 1
        if length == 0:
            inbalance = False
        else:
            inbalance = (result[0][1] / length) > 0.5
            inbalance |= (result[1][1] / length) > 0.5

        if inbalance:
            data.subtract(result[1][0])
            length -= 1
            _ += result[1][0]
        _ += ' '
    return _


def main():
    t = int(input())
    for i in range(1, t + 1):
        p = int(input())
        s = {str(chr(65+int(k))): int(v) for k, v in enumerate(input().split())}
        p = evac_plan(s)
        print("Case #{}: {}".format(i, p))

if __name__ == '__main__':
    main()