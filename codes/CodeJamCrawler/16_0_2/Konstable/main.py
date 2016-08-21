__author__ = 'OleksandrKonstantinov'

if __name__ == "__main__":
    with open("B-large.in", "r") as fRead, open("result.txt", "w") as fWrite:
        T = int(fRead.readline())
        for tc in range(1, T + 1):
            s = fRead.readline()
            l = []

            for ch in s:
                if ch == '+':
                    l.append(True)
                elif ch == '-':
                    l.append(False)

            size = len(l)
            res = 0

            while(True):

                index = size - 1
                while index >= 0:
                    if l[index] == False:
                        break
                    index -= 1

                if index == -1:
                    break

                for i in range (0, index + 1):
                    l[i] = not l[i]

                res += 1

            fWrite.write("Case #" + str(tc) + ": " + str(res) + "\n")