with open('in.txt') as f:
    lines = f.readlines()
lines = [l.split('\n')[0] for l in lines]
t = int(lines[0])


def find_number(s):
    original_s = s
    check_second = ["ONE", "THREE", "FIVE", "SEVEN", "NINE"]
    check_first = ["ZERO", "TWO", "FOUR", "SIX", "EIGHT"]
    num_dict = {
        "ZERO": 0,
        "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9}

    found_numbers = []
    while s:
        found1 = False
        for n in check_first:
            found = [-1] * len(n)
            for i, letter in enumerate(n):
                found[i] = s.find(letter)
                if found[i] == -1:
                    break
            if all(idx > -1 for idx in found):
                found_numbers.append(n)
                found1 = True
                s = ''.join([e for ii, e in enumerate(s) if ii not in found])
        if not found1 and s:
            break

    while s:
        for n in check_second:
            found = [-1] * len(n)
            for i, letter in enumerate(n):
                if n == 'THREE' and i == 4:
                    found[i] = s.find(letter, max(0, found[3] + 1))
                elif n == 'SEVEN' and i == 3:
                    found[i] = s.find(letter, max(0, found[1] + 1))
                elif n == 'NINE' and i == 2:
                    found[i] = s.find(letter, max(0, found[0] + 1))
                else:
                    found[i] = s.find(letter)
                if found[i] == -1:
                    break
            if all(idx > -1 for idx in found):
                found_numbers.append(n)
                s = ''.join([e for ii, e in enumerate(s) if ii not in found])

    found_nn = [num_dict[f] for f in found_numbers]
    sn = sorted(found_nn)
    sn = ''.join([str(sss) for sss in sn])
    return sn


f = open('out.txt', 'w')
for i in xrange(1, t + 1):
    f.write('Case #%s: %s \n' % (i, find_number(lines[i])))
    print 'Case #%s: %s' % (i, find_number(lines[i]))
f.close()
