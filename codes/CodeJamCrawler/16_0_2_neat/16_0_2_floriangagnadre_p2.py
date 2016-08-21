def get_cases(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        cases = []
        for t in range(T):
            cases.append(f.readline().rstrip())
        return T, cases

def count_flip(s):
    count = 0
    l = len(s)
    for i in range(l-1):
        if s[i] != s[i+1]:
            count += 1
    if (count%2 == 0) != (s[0] == '+'):
        count += 1
    return count

def b_print(res, T, filename):
    with open(filename, 'w') as f:
        for t in range(T):
            line = "Case #{0}: {1}".format(t+1, res[t])
            print(line)
            f.write(line + "\n")

if __name__ == '__main__':
    filename = 'B-large.in.txt'
    T, cases = get_cases(filename)
    res = [count_flip(s) for s in cases]
    b_print(res, T, 'outputp2-large.txt')