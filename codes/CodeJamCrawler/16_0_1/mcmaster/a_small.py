"""
Problem A

@author: Krisztian Balog
"""


def add_x(x, words):
    n = len(words)
    for i in range(n):
        wnew1 = x + words[i]
        wnew2 = words[i] + x
        words.append(wnew1)
        words.append(wnew2)

def solve(s):
    words = [""]
    for i in range(len(s)):
        add_x(s[i], words)
        if i == 0:
            del(words[0])
    #print(words)
    n = pow(2, len(s))
    lastwords = words[len(words)-n:len(words)] #[w in words for len(w) == n]
    lastwords.sort(reverse=True)
    #print(lastwords)

    return lastwords[0]


def run(infile, outfile):
    with open(infile, "r") as f:
        t = int(f.readline().strip())
        cases = [f.readline().strip() for i in range(t)]
    with open(outfile, "w") as f:
        for i, s in enumerate(cases):
            sol = solve(s)
            print(sol)
            f.write("Case #" + str(i + 1) + ": " + sol + "\n")


if __name__ == "__main__":
    run("A-small-attempt0.in", "A-small-attempt0.out")