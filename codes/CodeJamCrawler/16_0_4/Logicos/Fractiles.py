import re


# 1 = L
# 0 = G
def frac(basis, basis3):
    k = len(basis3) * "0"
    basis2 = re.sub("0", k, basis)
    basis = re.sub("1", basis3, basis2)
    return basis


def basissen(lengte):
    ret = set()
    for i in range(2 ** lengte, 2 * 2 ** lengte):
        ret.add(str(bin(i)[3:]))
        print(str(bin(i)[3:]))
    return ret


def fractal(basis, aantal):
    basis2 = basis
    for _ in range(aantal - 1):
        basis2 = frac(basis2, basis)
    return basis2


def fracs(basisLengte, aantal):
    ret = set()
    for basis in basissen(basisLengte):
        f = fractal(basis, aantal)
        print(f)
        ret.add(f)

    return ret


def test(setje, combinaties):
    i = False
    for combi in combinaties:
        booltje = False
        for getal in setje:
            if combi[getal - 1] == "0":
                booltje = True
        if not booltje:
            if i:
                return False
            else:
                i = True
    return setje


def setmaker(aantal, lengte):
    ret = []
    ret3 = []
    for i in range(1, lengte + 1):
        a = []
        a.append(i)
        ret.append(a.copy())
    ret3.extend(ret)
    for _ in range(aantal - 1):
        ret2 = []
        for setje in ret:
            for i in range(setje[-1], lengte + 1):
                a = setje.copy()
                if i not in a:
                    a.append(i)
                    ret2.append(a.copy())
        ret3.extend(ret2)
    print(ret2)
    return ret2


def Case(a, b, c, caseNr):
    sets = setmaker(c, a ** b)
    combinaties = fracs(a, b)
    for setje in sets:
        if test(setje, combinaties):
            res = test(setje, combinaties)
            ret = ""
            for item in res:
                ret += " " + str(item)
            print("Case #{}: {}".format(caseNr, ret[1:]))
            return
    print("Case #{}: {}".format(caseNr , "IMPOSSIBLE"))
    return


def Case2(a,b,c,caseNr):
        combinaties = fracs(a, b)
        print(combinaties)

aantal = int(input())
for l in range(aantal):
    inputstr = str(input())
    spl = inputstr.split(" ")
    ret = "Case #{}: 1".format(l + 1)
    for i in range(2,int(spl[0]) + 1):
        ret += " " + str(i)
    print(ret)