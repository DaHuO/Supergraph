# Read linescount
t = int(input())
for i in range(1, t + 1):
    pancakes = list(raw_input())
    lenLi = len(pancakes)
    count = 0

    while True:
        try:
            indexNeg = pancakes.index('-')
            count += 1
            try:
                indexPos = pancakes.index('+')
                #indexPos -= 1
                if indexPos == 0:
                    j = 0
                    while True:
                        if pancakes[j] == '+':
                            pancakes[j] = '-'
                            if pancakes[(j+1) % lenLi] == '-':
                                break
                        else:
                            pancakes[j] = '+'
                            if pancakes[(j+1) % lenLi] != '+':
                                break
                        j += 1
                else:
                    for j in range(0, indexPos):
                        if pancakes[j] == '+':
                            pancakes[j] = '-'
                            if pancakes[(j+1) % lenLi] == '-':
                                break
                        else:
                            pancakes[j] = '+'
                            if pancakes[(j+1) % lenLi] == '+':
                                break
            except ValueError:
                print("Case #{}: {}".format(i, count))
                break
        except ValueError:
            print("Case #{}: {}".format(i, count))
            break

