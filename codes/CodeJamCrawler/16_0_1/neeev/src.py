def init():
    f = open('in', 'r')

    f.readline()
    l = []

    for line in f:
        l.append(line)

    return l

def all_true(l):
    for e in l:
        if e==0:
            return 0
    return 1

def string_to_list(s, l):
    for c in s:
        l[int(c)] = 1
    return l

def debug_array(l):
    for e in l:
        print(e, end=" ")
    print("\n")

def result(a, i):
    if int(a)==0:
        r = "INSOMNIA"
    else:
        l = 10*[0]
        t = 0
        while all_true(l)==0:
            t += int(a)
            l = string_to_list(str(t), l)
        r = str(t)
    print("Case #" + str(i) + ": " + r)


def main():
    l = init()
    i = 1
    for a in l:
        result(a, i)
        i+=1


if __name__ == "__main__":
    main()
