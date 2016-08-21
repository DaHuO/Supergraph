with open("A-large.in", "r") as data:
    cases = int(data.readline())
    with open("A-large.out", "w") as result:
        for i in range(cases):
            word = data.readline().rstrip()
            res = ""
            for letter in word:
                if not res:
                    res = letter
                else:
                    if res[0] > letter:
                        res = res + letter
                    else:
                        res = letter + res
            result.write("Case #" + str(i+1) + ": " + res + "\n")
