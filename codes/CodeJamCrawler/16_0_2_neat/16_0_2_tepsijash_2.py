import fileinput

fin = fileinput.input()

def merge(s):
    ret = ""
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] != s[i + 1]:
            ret = ret + s[i]
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i = i + 1
    return ret + s[len(s) - 1]

def main():
    fin = fileinput.input()
    T = int(next(fin))  # number of test cases
    for case in range(1, T + 1):
        s = next(fin)
        s = merge(s.strip())
        N = len(s) - 1 + (s[len(s)-1] == '-')
        print("Case #{}: {}".format(case, N))

if __name__ == '__main__':
    main()
