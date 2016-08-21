import sys
in_file = open("test.txt")
#in_file = sys.stdin



def str_to_bit(s):
    lister = []
    for c in s:
        if c == '+':
            lister.append(1)
        else:
            lister.append(0)
    return lister

def NOT(num):
    if num:
        return 0
    return 1

def flip(lister, ind):
    new_lister = lister[:]

    for i in range(ind+1):
        new_lister[i] = NOT(lister[ind - i])

    return new_lister



def solve(s):

    lister = str_to_bit(s)

    n = len(lister)

    cur = n-1
    ans = 0
    looking = 1

    while cur >= 0:

        while cur >= 0 and lister[cur] == looking:
            cur -= 1

        if cur < 0:
            break

        # LANDED ON SOMETHING NOT EQUAL

       # print cur,looking
        if lister[0] == NOT(looking):
            ans += 1
            lister = flip(lister, cur)
        else:
            ans += 1
            looking = NOT(looking)

    return ans


#out = sys.stdout
out = open("OUTPUT.txt", "w")


data = in_file.read().strip().split()[1:]

for i in range(len(data)):
    out.write("Case #%i: %i\n" %(i+1, solve(data[i])))
