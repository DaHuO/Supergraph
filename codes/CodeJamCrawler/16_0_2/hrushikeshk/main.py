def opp(ch):
    if ch == '+':
        return '-'
    else:
        return '+'


def flip(ls, num):
    for j in range((num + 1) // 2):
        temp = opp(ls[j])
        ls[j] = opp(ls[num - j])
        ls[num - j] = temp
        ''.join(ls)
    if num % 2 == 0:
        ls[num // 2] = opp(ls[num // 2])


test = int(raw_input())

for case in range(1, test + 1):
    pancakes = list(raw_input())

    flag = False        # TO check whether all are happy side up
    all_same = False
    count = 0

    while True:
        temp = pancakes[0]
        for char in range(len(pancakes)):
            if temp != pancakes[char]:
                flip(pancakes, char - 1)
                count += 1
                all_same = False
                break
            else:
                all_same = True
                continue

        if all_same:
            if pancakes[0] == "-":
                count += 1
                flag = True
            else:
                flag = True

        if flag:
            print "Case #" + str(case) + ": " + str(count)
            break

