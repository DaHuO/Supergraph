
def move_pancake(data):
    new_data = data.split('+')
    st, ce =1, 2
    count = len([i for i in new_data if i])
    if new_data[0]:
        return st + (ce * (count - 1))
    else:
        return ce * count

input = (open(r'C:\Users\prakaran\Downloads\B-large.in', 'r').read().strip()).split('\n')
with open('blarge1.txt', 'wb') as f:
    for i in xrange(1, int(input[0]) + 1):
        if '-' in input[i]:
            val = move_pancake(input[i].strip())
            f.write("Case #%s: %s\n" % (i, val))
        else:
            f.write("Case #%s: 0\n" % i)