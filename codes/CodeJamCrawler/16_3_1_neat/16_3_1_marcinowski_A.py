letters = [chr(i) for i in range(65,91)]

def reader(file):
    f = open(file,'r')
    f_out = file[:-2]+"out"
    T = int(f.readline())
    cases = []
    for t in range(T):
        N = int(f.readline())
        case = f.readline().strip().split(' ')
        for i in range(len(case)):
            case[i] = int(case[i])
        cases.append(case)
    return cases, f_out

def solver(cases, f_out):
    f_out = open(f_out, 'w')
    for c in range(len(cases)):
        case = cases[c]
        print("Case #{}: ".format(c + 1), end='', file=f_out)
        while len(case) > case.count(0):

            if len(case) - case.count(0) == 2:
                result = ''
                for i in range(len(case)):
                    if case[i] != 0:
                        result += letters[i]
                        case[i] -= 1
                print(result, sep=' ', end=' ', file=f_out)
            elif len(case) - case.count(0) > 2:
                m_case = max(case)
                m_ind = case.index(m_case)
                try:
                    m_rest = max(max(case[:m_ind]), max(case[m_ind + 1:]))
                except ValueError:
                    try:
                        m_rest = max(case[:m_ind])
                    except ValueError:
                        m_rest = max(case[m_ind:])
                if m_case == m_rest:
                    print(letters[m_ind], sep=' ', end=' ', file=f_out)
                    case[m_ind] -= 1
                else:
                    print(letters[m_ind], sep=' ', end=' ', file=f_out)
                    case[m_ind] -= 1
        print('', file=f_out)


def main():
    cases, f_out = reader('A-large.in')
    solver(cases, f_out)

main()


