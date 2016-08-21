# Input files
fin = open('phone.in', 'r')
fout = open('phone.out', 'w')

digitsMap = {0: "ZERO",
             1: "ONE",
             2: "TWO",
             3: "THREE",
             4: "FOUR",
             5: "FIVE",
             6: "SIX",
             7: "SEVEN",
             8: "EIGHT",
             9: "NINE"}

T = int(fin.readline())


def contains(S, d):
    digit = digitsMap[d]
    for c in digit:
        if c not in S:
            return False
        else:
            S = S.replace(c, "", 1)

    return True


def remove(S, d):
    digit = digitsMap[d]
    for c in digit:
        S = S.replace(c, "", 1)
    return S


for t in range(0, T):
    S = fin.readline()
    tempS = S
    phone = ""
    d = 0
    digits = [6, 8, 3, 2, 0, 4, 7, 1, 5, 9]
    while d < 10:
        if contains(tempS, digits[d]):
            phone += str(digits[d])
            tempS = remove(tempS, digits[d])
        else:
            d += 1
    phone = "".join(sorted(phone))
    #print(S + " " + tempS + " " + phone + "\n" + "*******" + "\n")

    fout.write("Case #" + str(t+1) + ": " + phone + "\n")

# Output files
fin.close()
fout.close()