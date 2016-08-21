def main():
    caseCounter = 1
    outFile = open('out.txt', 'w')
    with open('sheep.txt') as f:
        cases = int(next(f))
        for case in f:
            start = int(case)
            base = start
            seen = set()
            finish = False
            inc = 1

            while (finish != True):
                if start == 0:
                    outFile.write('Case #' + str(caseCounter) + ': INSOMNIA\n')
                    finish = True
                else:
                    number = start
                    while number:
                        digit = number % 10
                        seen.add(digit)
                        number //= 10
                    if len(seen) == 10:
                        outFile.write('Case #' + str(caseCounter) + ': ' + str(start) + '\n')
                        finish = True
                    else:
                        start = base * (inc + 1)
                        inc += 1
            caseCounter += 1
    outFile.close()

if __name__ == "__main__":
    main()