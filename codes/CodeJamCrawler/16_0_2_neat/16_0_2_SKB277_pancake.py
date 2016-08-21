def do_flip(stack, too):
    l1 = stack[0:too]
    l2 = stack[too:]
    l1.reverse()
    l1 = list(map(lambda x: x*(-1), l1))
    return l1 + l2


def top_is_happy(stack):
    counter = 0
    while True:
        if counter > len(stack)-1:
            counter = -1
            break
        if stack[counter] == -1:
            break
        counter += 1
    return counter


def top_is_sad(stack):
    counter = 0
    while True:
        if counter > len(stack)-1:
            counter = -1
            break

        if stack[counter] == 1:
            break
        counter += 1
    return counter


def pancakes(L):
    flips = 0
    while True:
        if L[0] == 1:
            result = top_is_happy(L)
            if result < 0:
                break
            else:
                L = do_flip(L, result)
                flips += 1
        else:
            result = top_is_sad(L)
            if result < 0:
                flips += 1
                break
            else:
                L = do_flip(L, result)
                flips += 1
    return str(flips)


def main():
    f = open('B-small-attempt0.in', 'r')
    w = open('out.txt', 'w')
    i = 0
    for line in f:
        if i:
            tray = []
            for k in line:
                if k == "-":
                    tray.append(-1)
                elif k == "+":
                    tray.append(1)
            answer = "Case #"+str(i)+": " + pancakes(tray)
            w.write(answer + "\n")
        i += 1
    f.close()
    w.close()

main()
