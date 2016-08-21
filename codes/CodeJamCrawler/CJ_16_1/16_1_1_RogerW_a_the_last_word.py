def main():
    t = int(raw_input())  # read a line with a single integer
    for caseIdx in xrange(1, t + 1):
        S = raw_input()

        if len(S) <= 1:
            lastWord = S
        else:
            lastWord = S[0]
            for i in xrange(1,len(S)):
                if S[i] >= lastWord[0]:
                    lastWord = S[i] + lastWord
                else:
                    lastWord = lastWord + S[i]

        print "Case #{}: {}".format(caseIdx, lastWord)

if __name__ == '__main__':
    main()
