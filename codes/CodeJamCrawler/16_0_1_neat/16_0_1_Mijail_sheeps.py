def CountSheeps(n):
    digits_seen = [False, False, False, False, False,
                   False, False, False, False, False]
    if n == 0:
        return "INSOMNIA"
    i = 1
    left_digits = 10
    original_n = n
    while i <= 1000:
        n = i * original_n
        str_n = str(n)
        for character in str_n:
            if not digits_seen[int(character)]:
                left_digits -= 1
                digits_seen[int(character)] = True
            if left_digits == 0:
                return str_n
        i += 1
    return "INSOMNIA"


with open("A-large.in") as f:
    data = f.readlines()
    T = data[0]
    fh = open("finalNumbers", "w")
    linesToWrite = []
    for i in range(1, len(data)):
        finalNumber = CountSheeps(int(data[i]))
        print str(i)
        linesToWrite.append("Case #" + str(i) + ": " + finalNumber + "\n")
    linesToWrite[len(linesToWrite) - 1] = linesToWrite[len(linesToWrite) - 1].replace("\n", "")
    fh.writelines(linesToWrite)
    fh.close()
