def main():
    i = 0
    while True:
        try:
            t = input()
            if i != 0:  # Skip first line
                print("Case #{}: {}".format(i, lastword(t)))
        except EOFError:
            break
        i += 1


def lastword(s):
    x = []
    for c in list(s.rstrip()):
        if len(x) > 0 and c >= x[0]:
            x.insert(0, c)
        else:
            x.append(c)
    return "".join(x)

if __name__ == "__main__":
    main()
