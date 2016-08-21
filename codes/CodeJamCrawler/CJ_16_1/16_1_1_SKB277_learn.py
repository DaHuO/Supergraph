def last_word(s):
    res = ""
    for i in s:
        if res != '':
            if res[0] <= i:
                res = i + res
            else:
                res += i
        else:
            res += i
    return res


def main():
    f = open('A-small-attempt0.in', 'r')
    w = open('out.txt', 'w')
    i = 0
    for line in f:
        if i:
            answer = "Case #"+str(i)+": " + last_word(line)
            w.write(answer + "\n")
        i += 1
    f.close()
    w.close()

main()
