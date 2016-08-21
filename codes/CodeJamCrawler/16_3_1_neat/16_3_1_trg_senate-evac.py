import sys
from collections import Counter


def generate_evac_plan(party_cnt):
    party_cnt = party_cnt.copy()
    party_sum_even = sum(party_cnt.values()) % 2 == 0

    while True:
        if party_sum_even:
            pairs1 = party_cnt.most_common(1)
        else:
            pairs1 = party_cnt.most_common(3)

            if all(pair[1] == 1 for pair in pairs1):
                # speciall case for odd sums
                p1 = pairs1[0][0]
                yield p1, None
                party_cnt[p1] -= 1
                continue

        if pairs1[0][1] == 0:
            break
        p1 = pairs1[0][0]
        party_cnt[p1] -= 1
        pairs2 = party_cnt.most_common(1)
        if pairs2[0][1] == 0:
            p2 = None
        else:
            p2 = pairs2[0][0]
            party_cnt[p2] -= 1
        yield p1, p2


def get_evac_str(p1, p2):
    if p2:
        return '{}{}'.format(p1, p2)
    else:
        return p1


def print_evac_plan(case_num, evac_plan):
    evac_plan_str = ' '.join(get_evac_str(p1, p2) for p1, p2 in evac_plan)
    print('Case #{}: {}'.format(case_num + 1, evac_plan_str))


def construct_party_cnt(party_nums):
    cnt = Counter()
    ord_A = ord('A')
    for i, num in enumerate(party_nums):
        party = chr(ord_A + i)
        cnt[party] = num
    return cnt


def main():
    line_iter = iter(sys.stdin)
    T = int(next(line_iter))
    for i in range(T):
        N = int(next(line_iter))
        PN = [int(elem) for elem in next(line_iter).strip().split()]
        assert(len(PN) == N)
        party_cnt = construct_party_cnt(PN)
        evac_plan = generate_evac_plan(party_cnt)
        print_evac_plan(i, evac_plan)


if __name__ == '__main__':
    main()
