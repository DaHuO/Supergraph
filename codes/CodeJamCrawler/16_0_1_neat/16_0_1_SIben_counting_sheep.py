def parsing():
    nb_tests = int(raw_input())
    cases = []

    for _ in range(nb_tests):
        cases.append(int(raw_input()))

    return nb_tests, cases

def display(case_number, result):
    print "Case #" + str(case_number) + ": " + str(result)

def main():
    nb_tests, cases = parsing()

    results = []

    for i in range(nb_tests):
        sn = cases[i]
        seen = {}

        if sn == 0:
            results.append(-1)
            continue

        cn = 0
        while len(seen) != 10:
            cn += sn
            str_sn = str(cn)
            for idx in range(len(str_sn)):
                seen[str_sn[idx]] = True

        results.append(cn)

    for i in range(nb_tests):
        if results[i] == -1:
            display(i + 1, "INSOMNIA")
        else:
            display(i + 1, results[i])

if __name__=='__main__':
    main()
