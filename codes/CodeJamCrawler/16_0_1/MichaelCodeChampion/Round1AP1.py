def solve(n):
    #sol = []
    d = 1

    all = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    word  = n[0][0]
    number = 0
    n = n[0]
    for i in range(len(all)):
        if all[i] == word:
            number = i
            break

    n = n[1:]
    print(word)
    for i in range(len(n)):
        print(number)
        for j in range(len(all)):
            if all[j] == n[i]:
                number2 = j
                print(number2)
                break
        if number2>=number:
            word = n[i] + word
            number = number2
        else:
            word = word + n[i]



    print(word)
    return d, word



IN = open('input.txt', 'r')
OUT = open('output.txt', 'w')

T = int(IN.readline())

for line in range(T):
    # Instanz mit mehreren Zeilen
    yes = 0
    if yes == 0:
        #sizen = int(IN.readline())
        n = list(map(str, IN.readline().split()))
    else:
        T0 = int(IN.readline())
        n = []
        for i in range(T0):
            n.append(list(map(int, IN.readline().split())))

    if solve(n)[0] == 1:
        answer = solve(n)[1]#' '.join(map(str,solve(n)[1]))
        OUT.write('Case #{}: {}\n'.format(line + 1, answer))
    else:
        OUT.write('Case #{}:\n'.format(line + 1))
        for i in range(len(solve(n)[1])):
            answer = ' '.join(map(str,solve(n)[1][i]))
            OUT.write('{}\n'.format(answer))
    if yes == 1:
        line -= T0
IN.close()
OUT.close()