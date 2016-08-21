__author__ = 'smirzai'



def solve(st):
    s = list(st)

    level1 = [["Z", "ZERO", 0], ["W", "TWO", 2], ["U", "FOUR", 4], ["X", "SIX", 6], ["G", "EIGHT", 8]]
    level2 = [["O", "ONE", 1], ["H", "THREE", 3], ["F", "FIVE", 5], ["V", "SEVEN", 7]]
    level3 = [["T", "TEN", 10]]
    level4 = [["N", "NINE", 9]]
    levels = level1 + level2 + level3 + level4

    i = 0
    result = []

    while i <= 10:

        while levels[i][0] in s:
            result.append(levels[i][2])
            for ch in levels[i][1]:
                if ch in s:
                    s.remove(ch)
        i += 1


    return  result

filename = "small2"

f = open(filename, "r")

n = f.readline()
n = int(n)
import sys



o = open("A-small-attempt1.out", "w")
#o = sys.stdout



for i in range(n):
    st = f.readline()
    result = solve(st)
    result = sorted(result)
    result = map(str, result)

    o.write("Case #"  + str(i+1) + ": " + "".join(result) + "\n")


o.close()
f.close()
