import sys


def count_lets(txt):
    cnt = {}
    for c in txt:
        if c not in cnt:
            cnt[c] = 0
        cnt[c] += 1
    return cnt

texts = [
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
]

lcounts = []
for n in texts:
    lcounts.append(count_lets(n))

def subtract(cnt1, cnt2, mult=1):
    for k, v in cnt2.iteritems():
        cur_cnt = cnt1.get(k, 0)
        mv = v*mult
        if cur_cnt < mv:
            return None
        cnt1[k] -= mv

    return cnt1

def sub_number(indicator, idx, cnts):
    num = cnts.get(indicator, 0)
    if num == 0:
        return (idx, 0)
    subtract(cnts, lcounts[idx], num)
    return (idx, num)

def find_sol(text):
    cnts = count_lets(text)

    rs = []
    rs.append(sub_number('X', 6, cnts))

    rs.append(sub_number('G', 8, cnts))

    rs.append(sub_number('W', 2, cnts))

    rs.append(sub_number('Z', 0, cnts))

    rs.append(sub_number('U', 4, cnts))

    rs.append(sub_number('F', 5, cnts))

    rs.append(sub_number('V', 7, cnts))

    rs.append(sub_number('H', 3, cnts))

    rs.append(sub_number('O', 1, cnts))

    rs.append(sub_number('I', 9, cnts))

    rs = sorted(rs)

    return "".join(["".join([str(i)]*n) for i, n in rs])



def parse_file(fname):
    with open(fname, "r") as fh:
        lines = fh.readlines()[1:]

    return lines

def process(n):
    return find_sol(n)

def main():
    fname = sys.argv[1]
    outname = sys.argv[2]

    ns = parse_file(fname)

    answers = [process(n) for n in ns]

    with open(outname, "w") as fh:
        for i, a in enumerate(answers, 1):
            fh.write("Case #%i: %s\n" % (i, a))


if __name__ == "__main__":
    main()
