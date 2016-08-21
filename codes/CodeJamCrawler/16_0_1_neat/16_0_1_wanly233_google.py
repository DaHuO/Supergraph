def countSheep(num):
    s = set()
    i = 1
    while len(s) != 10:
        if not num: break
        curr = i * num
        for c in str(curr): s.add(c)
        i += 1
        # print curr, s 
    return str(curr) if num else "INSOMNIA"

out = open("res-Large.out", 'w')
if __name__ == '__main__':
    with open("A-large.in") as f:
        args = f.readlines()[1:]
        for i in range(len(args)):
            args[i] = int(args[i])
            res = countSheep(args[i])
            out.write("Case #{}: {}\n".format(i + 1, res))