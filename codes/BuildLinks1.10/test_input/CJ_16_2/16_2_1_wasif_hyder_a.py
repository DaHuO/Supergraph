from collections import Counter

d = {
    0:("ZERO", "Z"),
    2:("TWO", "W"),
    4:("FOUR", "U"),
    6:("SIX", "X"),
    8:("EIGHT", "G"),
    5:("FIVE", "F"),
    7:("SEVEN", "S"),
    3:("THREE","H"),
    9:("NINE","I"),
    1:("ONE","O")

}

def solution(s):
    s = Counter(s)
    result = ""
    for i in [0, 2, 4, 6, 8, 5, 7, 3, 9, 1]:
        letter = d[i][1]
        numchars = Counter(d[i][0])
        if letter in s and s[letter] != 0:
            repetitions = s.get(d[i][1], 0)
            for j in range(repetitions):
                s.subtract(numchars)
                result += str(i)
    return "".join([x for x in sorted(list(result))])


with open('a.in', 'r') as fin:
    fout = open('a.out', 'w')
    n = int(fin.readline())

    for case in range(n):
        s = fin.readline().rstrip()
        result = solution(s)

        print("Case #{}: {}".format(case+1, result))
        fout.write("Case #{}: {}\n".format(case+1, result))
