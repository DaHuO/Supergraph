def charCountDict(s):
    ccd = {}
    for ch in s:
        if ch not in ccd:
            ccd[ch] = 1
        else:
            ccd[ch] += 1
    return ccd

if __name__ == "__main__":
    digits = [
        "ZERO",
        "ONE",
        "TWO",
        "THREE",
        "FOUR",
        "FIVE",
        "SIX",
        "SEVEN",
        "EIGHT",
        "NINE"
    ]

    dcc = {}
    for i in range(10):
        dcc[i] = charCountDict(digits[i])

    levelOne = {
        "Z": 0,
        "W": 2,
        "U": 4,
        "X": 6,
        "G": 8
    }
    levelTwo = {
        "O": 1,
        "H": 3,
        "F": 5,
        "S": 7
    }

    t = int(input().strip())
    for case_no in range(1, t + 1):
        s = input().strip()
        # print("s {}".format(s))
        sChDict = charCountDict(s)
        actDigits = []

        # level one
        for ch, digit in levelOne.items():
            if ch in sChDict and sChDict[ch] > 0:
                # print("appending {} to actDigits".format(ch))
                cnt = sChDict[ch]
                for _ in range(cnt):
                    actDigits.append(digit)
                digitCharCountDict = dcc[digit]
                for chOfDigit in digitCharCountDict:
                    sChDict[chOfDigit] -= cnt

        # level two
        for ch, digit in levelTwo.items():
            if ch in sChDict and sChDict[ch] > 0:
                # print("appending {} to actDigits".format(ch))
                cnt = sChDict[ch]
                for _ in range(cnt):
                    actDigits.append(digit)
                digitCharCountDict = dcc[digit]
                for chOfDigit in digitCharCountDict:
                    sChDict[chOfDigit] -= cnt

        if "I" in sChDict and sChDict["I"] > 0:
            for i in range(sChDict["I"]):
                actDigits.append(9)

        actDigits.sort()
        print("Case #{}: {}".format(str(case_no), "".join(str(x)
                                                          for x in actDigits)))
