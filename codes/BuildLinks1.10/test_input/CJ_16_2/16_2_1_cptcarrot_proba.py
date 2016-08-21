names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE",
         "SIX", "SEVEN", "EIGHT", "NINE"]
letters_list = [list(set(s)) for s in names]
order = [0, 2, 6, 7, 8, 3, 5, 4, 1, 9]
unique = ['Z', 'W', 'X', 'S', 'G', 'H', 'V', 'R', 'O', 'I']

def replace_num(num, cnt, s):
    letters = letters_list[num]
    for c in letters:
        s = s.replace(c, '', names[num].count(c)*cnt)
    return s

def make_num(count):
    res = ''
    for i in range(10):
        res = res + str(i)*count[i]
    return res

def solve():
    infile = open("A-large.in")
    outfile = open("A-large.out", 'w')
    T = int(infile.readline().strip())
    for i in range(T):
        occur = [0] * 10
        s = infile.readline().strip()
        for j in range(10):
            num = order[j]
            occur[num] = s.count(unique[j])
            if occur[num] != 0:
                s = replace_num(num, occur[num], s)
        res = "Case #%d: %s\n" % (i+1, make_num(occur))
        outfile.write(res)
    infile.close()
    outfile.close()

solve()
