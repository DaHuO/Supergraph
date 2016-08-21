def parsing():
    nb_tests = int(raw_input())
    cases = []

    for _ in range(nb_tests):
        cases.append(raw_input())

    return nb_tests, cases

def display(case_number, result):
    print "Case #" + str(case_number) + ": " + str(result)

def solve_alter(case):
    
    cnt = 0

    for idx in range(len(case)):
        if case[idx] == '-':
            cnt += 2

    if case[0] == '-':
        cnt -= 1

    return cnt

def main():
    nb_tests, cases = parsing()
    results = []
   
    for i in range(nb_tests):
        c = cases[i]
        case = ''.join([c[0]] +
                       [c[j] for j in range(1, len(c)) if c[j] != c[j - 1]])
        results.append(solve_alter(case))

    for i in range(nb_tests):
        display(i + 1, results[i])

if __name__=='__main__':
	main()
