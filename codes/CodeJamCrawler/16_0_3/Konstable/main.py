__author__ = 'OleksandrKonstantinov'
import math

def PrimeFactor(p):
    sp = int(math.sqrt(p))
    for num in range(2, sp + 1):
        if (p % num) == 0:
            return num

    return 1



if __name__ == "__main__":
    with open("result.txt", "w") as fWrite:

        N = 50
        Ans = []

        fWrite.write("Case #1:\n")
        string = "1000000000000001"
        while (string <= "1111111111111111"):
            factors = []
            for base in range(2, 11):
                p = int(string, base)
                factor = PrimeFactor(p)
                if (factor == 1):
                    break
                factors.append(str(factor))

            if (len(factors) == 9):
                fWrite.write(string + " " + str(" ".join(factors)) + "\n")
                Ans.append(string)
                if (len(Ans) == N):
                    break

            a = int(string, 2)
            a += 2
            string = str(bin(a))[2:]



