def flip(s, index):
    for i in range(int(index / 2) + 1):
        temp = s[i]
        s[i] = (s[index] == '+' and '-' or '+')
        s[index] = (temp == '+' and '-' or '+')
    # print(''.join(s))

def count_flip(str):
    s = list(str)
    # print(''.join(s))
    first_side = s[0] == '+' and True or False
    count = 0
    for i in range(len(s)):
        if i == 0:
            continue
        if first_side == (s[i] == '+' and True or False):
            continue
        else:
            # flip(s, i - 1)
            first_side = not first_side
            count += 1
            continue

    if first_side == False:
        # flip all
        first_side = not first_side
        count += 1

    return count

def test():
    #test_cases = [["-", 1], ["-+", 1], ["+-", 2], ["+++", 0], ["--+-", 3]]
    print("start test")
    test_cases = [["+", 0], ["-", 1],
                  ["++", 0], ["+-", 2], ["-+", 1], ["--", 1],
                  ["+++", 0], ["++-", 2], ["+-+", 2], ["+--", 2],
                  ["-++", 1], ["-+-", 3], ["--+", 1], ["---", 1]]
    for test_case in test_cases:
        try:
            assert count_flip(test_case[0]) == test_case[1]
            print("pass")
        except:
            print("%s expected=%d actual=%d" % (test_case[0], test_case[1], count_flip(test_case[0])))
    print("finish test")
#test()


t = int(input())

for i in range(t):
    s = input()

    count = count_flip(s)
    print("Case #%d: %s" % (i + 1, count))
