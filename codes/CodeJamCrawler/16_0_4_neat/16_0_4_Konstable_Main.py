__author__ = 'OleksandrKonstantinov'

if __name__ == "__main__":
    with open("D-small-attempt0.in.txt", "r") as fRead, open("result.txt", "w") as fWrite:
        T = int(fRead.readline())
        for tc in range(1, T + 1):
            k, c, s = [int(x) for x in fRead.readline().split()]
            if (s == 0):
                fWrite.write("Case #" + str(tc) + ": IMPOSSIBLE")
                continue

            if (k == s):
                fWrite.write("Case #" + str(tc) + ": 1")
                for i in range(2, k + 1):
                    fWrite.write(" " + str(i))
                fWrite.write("\n")
            else:
                raise InterruptedError("baad")
