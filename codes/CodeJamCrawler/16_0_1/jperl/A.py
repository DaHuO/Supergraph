# competition io code from https://github.com/DarioFanucchi/CompetitionCode.git
import codejam_io


def addDigits(num, seen):
    for digit in str(num):
        if digit not in seen:
            seen.append(digit)
    return seen

def countSheep(N):
    seenNums = []
    for i in xrange(1, 100000):
        seenNums = addDigits(i*N, seenNums)
        if len(seenNums) == 10:
            break
    if i == 99999:
        return "INSOMNIA"
    else:
        return i*N

ans = []
for case in codejam_io.read_straight("A-large.in"):
    ans.append(countSheep(int(case)))

codejam_io.write_simple("A_large.out", ans)


