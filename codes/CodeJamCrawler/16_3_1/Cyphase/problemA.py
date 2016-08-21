from __future__ import print_function

import sys

try:
    input = raw_input
except NameError:
    pass


def main():
    num_cases = input()

    for case_idx, s in enumerate(iter(sys.stdin.readline, ''), 1):
        P_letters = list('ABCDEFGHIJJKLMNOPQRSTUVWXYZ')
        P_counts = list(map(int, input().strip().split()))

        P = dict(zip(P_letters, P_counts))

        instructions = []

        while len(set(P.values())) > 1:
            max_party, max_count = max(P.items(), key=lambda x: x[1])
            instructions.append(max_party)
            P[max_party] -= 1

        for party in [p for p, c in list(P.items()) if c > 0][:-2]:
            instructions.extend([party] * P[party])
            P[party] -= P[party]  # = 0

        parties = [p for p, c in list(P.items()) if c > 0]  # 2 left
        final_instruction = ''.join(p for p in parties)
        instructions.extend([final_instruction] * P[p])

        print("Case #{}: {}".format(case_idx, ' '.join(instructions)))


if __name__ == '__main__':
    main()
