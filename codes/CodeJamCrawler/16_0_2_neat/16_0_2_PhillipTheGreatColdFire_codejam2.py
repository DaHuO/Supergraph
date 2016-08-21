def fun(x):
    count = 0
    x = list(x)
    x.reverse()
    for i in range(len(x)):
        if x[i] == "-":
            count += 1
            for j in range(i,len(x)):
                if x[j] == "+":
                    x[j] = "-"
                else:
                    x[j] = "+"
        else:
            pass
    return count

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())

    for case in range(1,T+1):
        x = f.readline()
        answer = fun(x)
        print("Case #{0}: {1}".format(case, answer))
