#! python3

def main():
    with open("A-large.in") as in_file:
        with open("A-large.out", "w") as fout:
            cases = int(in_file.readline())
            for x in range(cases):
                num = str(in_file.readline().strip())
                onum = num
                numbers = []
                while len(num):
                    numSet = set(num)
                    replace = ""
                    replaceNum = 0
                    if "Z" in numSet:
                        replace = "ZERO"
                        replaceNum = 0
                    elif "U" in numSet:
                        replace = "FOUR"
                        replaceNum = 4
                    elif "W" in numSet:
                        replace = "TWO"
                        replaceNum = 2
                    elif "O" in numSet and "N" in numSet:
                        replace = "ONE"
                        replaceNum = 1
                    elif "R" in numSet:
                        replace = "THREE"
                        replaceNum = 3
                    elif "F" in numSet:
                        replace = "FIVE"
                        replaceNum = 5
                    elif "V" in numSet:
                        replace = "SEVEN"
                        replaceNum = 7
                    elif "X" in numSet:
                        replace = "SIX"
                        replaceNum = 6
                    elif "G" in numSet:
                        replace = "EIGHT"
                        replaceNum = 8
                    else:
                        replace = "NINE"
                        replaceNum = 9
                    numbers.append(replaceNum)
                    for c in replace:
                        num = num.replace(c, "", 1)

                fout.write("Case #{0}: {1}\n".format(x + 1, "".join([str(n) for n in sorted(numbers)])))

if __name__ == "__main__":
    main()
