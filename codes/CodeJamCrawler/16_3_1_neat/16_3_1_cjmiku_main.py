#!/usr/bin/env python

import fileinput

def tr(i):
    return chr(65 + i)

def trl(l):
    return ''.join(chr(65 + i) for i in l)


def isvalid(sens):
    for i, s in enumerate(sens):
        if sum(sens[:i] + sens[i + 1:]) < s * 0.5:
            return False
    return True

def evacuate(s):
    result = []
    senators = [j for j in s]
    while True:
        # print(senators)
        if sum(senators) == 0:
            # print('done.\n')
            break

        top2 = sorted(range(len(senators)), key=lambda i: senators[i], reverse=True)[:2]

        next = [j for j in senators]
        next[top2[0]] = next[top2[0]] - 1
        next[top2[1]] = next[top2[1]] - 1

        if isvalid(next):
            # print(trl(top2))
            result.append(trl(top2))
            senators = next
            continue # evacuate(next)

        next = [j for j in senators]
        next[top2[0]] = next[top2[0]] - 1

        if isvalid(next):
            # print(trl(top2[:1]))
            result.append(trl(top2[:1]))
            # print(top2[0])
            senators = next
            # evacuate(next)
    return result

if __name__ == '__main__':
    case = 1
    for i, line in enumerate(map(str.strip, fileinput.input())):
        if i == 0:
            continue
        if i % 2 == 1:
            continue
        result = evacuate(map(int, line.split()))
        print("Case #%s: %s" % (case, ' '.join(result)))
        case += 1

