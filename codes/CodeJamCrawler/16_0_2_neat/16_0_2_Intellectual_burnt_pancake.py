q = []
with open('B-large.in', 'rb') as f:
    count = 0
    for i in f:
        if count == 0:
            count = 1
            continue
        i = (i.strip().decode("utf-8"))
        q.append(i)


def rev(s, end, start=0):
    new_rev = ''
    to_be_reversed = s[start:(end+1)]
    # rev = to_be_reversed[::-1]
    for i, val in enumerate(to_be_reversed):
        if val == '+':
            new_rev += '-'
        elif val == '-':
            new_rev += '+'
    new_rev = new_rev[::-1]
    return new_rev + s[end+1:]


def minus_index(s):
    s = s[::-1]
    f_rev = s.find('-')
    return (len(s) - f_rev - 1)


def burnt_pancake(s, count):
    # print(s)
    minus_ind = minus_index(s)
    if minus_ind == len(s):
        # print(count)
        return count
    if s[0] == '-':
        count = burnt_pancake(rev(s, minus_ind), count + 1)
    elif s[0] == '+':
        e = s.find('-') - 1
        # print(count + 1)
        count = burnt_pancake(rev(s, e), count + 1)
    return count

for i, s in enumerate(q):
    print("Case #{}: ".format(i+1) + str(burnt_pancake(s, 0)))
    # print(burnt_pancake(, 0))
# print(rev("+++--", 0))
