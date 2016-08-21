T = input()


def all_three_ones(senators):

    if senators[0][0] == 1 and senators[1][0] == 1 and senators[2][0] == 1:
        print senators[0][1],
        print senators[1][1] + senators[2][1],
        senators[:] = []
        return True

    return False


def update(senators):
    senators.sort(reverse=True)

    while len(senators) > 0:
        if senators[-1][0] == 0:
            senators.pop()
        else:
            break


def make_plan(senators):

    while len(senators) > 0:
        if len(senators) != 3:
            print senators[0][1] + senators[1][1],
            senators[0][0] -= 1
            senators[1][0] -= 1
            update(senators)
        elif not all_three_ones(senators):
            print senators[0][1] + senators[1][1],
            senators[0][0] -= 1
            senators[1][0] -= 1
            update(senators)
    print ""

for case in range(T):
    N = input()
    temp = map(int, raw_input().split())
    senators = []

    for i in range(N):
        senators.append([temp[i], chr(65 + i)])

    update(senators)
    print "Case #" + str(case + 1) + ":",
    make_plan(senators)
