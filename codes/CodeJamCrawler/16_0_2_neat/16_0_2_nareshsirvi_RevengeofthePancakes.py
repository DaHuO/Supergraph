
if __name__ == "__main__":
    T = input()
    for i in range(1, T + 1):
        S = list(raw_input().strip())

        count = 0
        while S:
            j = len(S) - 1
            while j >= 0:
                if S[j] == "-":
                    break
                j -= 1
            S = S[:j + 1]

            if len(S) == 0:
                break

            if S[0] == "-":
                for j in range(len(S)):
                    S[j] = "+" if S[j] == "-" else "-"
                S.reverse()
                count += 1
            else:
                for j in range(len(S)):
                    if S[j] == "-":
                        break
                    S[j] = "-"
                count += 1

        print "Case #%d: %d" % (i, count)
