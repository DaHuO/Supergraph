def count(file):
    L = [line.strip() for line in open(file, "r")]
    rstring = ""
    if L[0] != "0":
        sheeps = L[1: int(L[0])+1]
        for i in range(len(sheeps)):
            check = []
            case = i+1
            multiplier = 1
            sheep = int(sheeps[i])
            holder = sheep
            if sheep == 0:
                rstring += "Case #{}: INSOMNIA\n".format(case)
            else:
                while len(check) < 10:
                    string = str(sheep)
                    for x in string:
                        if x not in check:
                            check.append(x)
                    multiplier += 1
                    sheep = holder*(multiplier)
                rstring += "Case #{0}: {1}\n".format(case, holder*(multiplier-1))
    return rstring

if __name__ == "__main__":
    file = "A-large.in"
    print(count(file))
