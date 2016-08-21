# coding:utf-8

def solve(case):
    result = None
    if case == 0:
        result = 'INSOMNIA'
    else:
        s = set()
        count = 1
        num = case
        while len(s) != 10:
            num = count * case
            [s.add(int(i)) for i in str(num)]
            count += 1

        result = str(num)
    return result

if __name__ == '__main__':
    testcases = int(input())

    for caseNr in range(1, testcases+1):
        cipher = int(input())
        print("Case #%i: %s" % (caseNr, solve(cipher)))