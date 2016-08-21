import fileinput
f = fileinput.input()
T = int(f.readline())

numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
alphabets = set(list(''.join(numbers)))
number_char_counts = []
for i in range(10):
    number_char_counts.append(dict())
    for c in numbers[i]:
        number_char_counts[i][c] = number_char_counts[i].get(c, 0) + 1

counts = dict()

def solve1(num_list, i):
    m = min([counts[c] / cnt for c, cnt in number_char_counts[i].items()])
    if m > 0:
        for c, cnt in number_char_counts[i].items():
            counts[c] -= m * cnt
        num_list.append([i, m])

    if i == 9:
        for count in counts.values():
            if count > 0:
                return False
        return True
    if solve1(num_list, i+1):
        return True

    num_item = num_list.pop()
    num = num_item[0]
    num_cnt = num_item[1] - 1
    for c, cnt in number_char_counts[num_item[0]].items():
        counts[c] += cnt
    if num_cnt > 0:
        num_list.append([num, num_cnt])
        return solve1(num_list, num + 1)
    if num_item[0] == 9:
        return False
    return solve1(num_list, num_item[0] + 1)

def solve(S):
    counts.clear()
    for c in alphabets:
        counts[c] = 0
    for c in S:
        counts[c] = counts.get(c, 0) + 1
    num_list = []
    solve1(num_list, 0);
#    for i in range(10):
#        if solve1(num_list, i):
#            break
    return ''.join([str(num) * cnt for num, cnt in num_list])

for case in range(1,T+1):
    S = f.readline().strip()
    print "Case #%d: %s" % (case, solve(S))
