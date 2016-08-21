from time import sleep
def a (fname):
    fin = open(fname + ".in")
    lines = fin.readlines()
    T = int(lines[0])
    fout = open(fname + ".out", "w")
    for t in range(1, T+1):
        line = lines[t]
        N = int(line)
        print("line " + str(t))
        fout.write("Case #" + str(t) + ": " + sheep(N) + "\n")

def sheep(N):
    print (N)
    if N == 0:
        return "INSOMNIA"
    digits = [0,0,0,0,0,0,0,0,0,0]
    i = 1
    while 0 in digits:
        s = str(i*N)
        for c in s:
            j = int(c)
            if digits[j] == 0:
                digits[j] = int(s)
                print(digits)
        i = i + 1
        # input()
    return s


def b (fname):
    fin = open(fname + ".in")
    lines = fin.readlines()
    T = int(lines[0])
    fout = open(fname + ".out", "w")
    for t in range(1, T+1):
        line = lines[t]
        stack = [(c == "+") for c in line[:-1]]
        fout.write("Case #" + str(t) + ": " + str(flips(stack)) + "\n")
        print(t)

def flips(stack):
    print(stack)
    if False not in stack:
        return 0
    for i in range(len(stack)):
        ind = -1 * i - 1
        if stack[ind] == False:
            return 1 + flips([not b for b in stack[:ind]])

def c (fname):
    fin = open(fname + ".in")
    lines = fin.readlines()
    T = int(lines[0])
    fout = open(fname + ".out", "w")
    for t in range(1, T+1):
        l1 = lines[2*t-1].split()
        l = l1[0]
        x = l1[1]
        qs = lines[2*t].strip()
        fout.write("Case #" + str(t) + ": " + c_answer(l, x, qs) + "\n")

def simplify_quat(sgn, qpart, qs, x):
    if (len(qpart) == 1) and (x == 0):
        return (sgn, qpart, qs, 0)
    if (len(qpart) == 1):
        return simplify_quat(sgn, qpart + qs, qs, x - 1)
    a = qpart[0]
    b = qpart[1]

    mult_table = {('i', 'j'): (True, 'k'), ('i', 'k'): (False, 'j'), ('j', 'k'): (True, 'i'), ('j', 'i'): (False, 'k'),
                 ('k', 'i'): (True, 'j'), ('k', 'j'): (False, ('i'))}

    if (a == b):
        if (len(qpart) == 2) and (x == 0):
            return (not sgn, "1", qs, 0)
        if (len(qpart) == 2) and (x > 0):
            return simplify_quat(not sgn, qs, qs, x - 1)
        return (not sgn, qpart[2:], qs, x)
    sgn2, lett = mult_table[(a, b)]
    return (sgn2 == sgn, lett + qpart[2:], qs, x)

def c_answer(l, orig_x, orig_qs):
    sgn = True
    qs = orig_qs
    qpart = qs
    x = int(orig_x) - 1
    x = x%64
    while qpart[0] != 'i':
        sgn, qpart, qs, x = simplify_quat(sgn, qpart, qs, x)
        if len(qpart) + x * len(qs) < 3:
            return "NO"
    qpart = qpart[1:]
    if len(qpart) == 0:
        qpart = qs
        x = x - 1

    while qpart[0] != "j":
        sgn, qpart, qs, x = simplify_quat(sgn, qpart, qs, x)
        if len(qpart) + x * len(qs) < 2:
            return "NO"
    qpart = qpart[1:]
    if len(qpart) == 0:
        qpart = qs
        x = x - 1

    while qpart[0] != "k":
        sgn, qpart, qs, x = simplify_quat(sgn, qpart, qs, x)
        if len(qpart) + x * len(qs) == 0:
            return "NO"

    if len(qpart) == 1 and x == 0:
        return "YES"
    qpart = qpart[1:]
    if len(qpart) == 0:
        qpart = qs
        x = x - 1
    while (len(qpart) != 1 or x != 0):
        sgn, qpart, qs, x = simplify_quat(sgn, qpart, qs, x)

    if sgn and qpart == "1":
        return "YES"
    return "NO"
