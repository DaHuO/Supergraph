numbers = [
    ('Z', 'ZERO', '0'),
    ('W', 'TWO', '2'),
    ('G', 'EIGHT', '8'),
    ('X', 'SIX', '6'),
    ('S', 'SEVEN', '7'),
    ('V', 'FIVE', '5'),
    ('I', 'NINE', '9'),
    ('F', 'FOUR', '4'),
    ('H', 'THREE', '3'),
    ('O', 'ONE', '1')
    ]

def get_cases(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        cases = []
        for t in range(T):
            cases.append(f.readline().rstrip())
        return T, cases

def b_print(res, T, filename):
    with open(filename, 'w') as f:
        for t in range(T):
            f.write("Case #{0}: {1}\n".format(t+1, res[t]))

def get_phone_number(s):
    res = []
    i = 0
    while i < 10:
        while numbers[i][0] in s:
            res.append(numbers[i][2])
            for c in numbers[i][1]:
                s = s.replace(c,'',1)
        i += 1
    return ''.join(sorted(res))

if __name__ == '__main__':
    filename = 'A-large.in'
    T, cases = get_cases(filename)
    res = [get_phone_number(s) for s in cases]
    b_print(res, T, 'outputp1-large.txt')