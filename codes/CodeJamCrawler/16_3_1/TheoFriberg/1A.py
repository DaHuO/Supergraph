# Written for PyPy3

def toLetter(i):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
def remove(senators, senatorcount):
    i = 0
    maximum = 0
    lastGreatest = 0
    while i < len(senators):
        if senators[i] > senators[maximum]:
            maximum = i
        elif senators[i] == senators[maximum] and i > 0:
            lastGreatest = i
        i = i + 1
    if senators[lastGreatest] == senators[maximum]:
        if senators[maximum] == 1:
            if senatorcount > 3 and lastGreatest != maximum:
                senators[lastGreatest] = senators[lastGreatest]-1
                senators[maximum] = senators[maximum]-1
                return (lastGreatest, maximum)
            elif senatorcount == 2 and lastGreatest != maximum:
                senators[lastGreatest] = senators[lastGreatest]-1
                senators[maximum] = senators[maximum]-1
                return (lastGreatest, maximum)
            else:
                senators[maximum] = senators[maximum]-1
                return (maximum,)
        elif lastGreatest != maximum:
            senators[lastGreatest] = senators[lastGreatest]-1
            senators[maximum] = senators[maximum]-1
            return (lastGreatest, maximum)
        else:
            senators[maximum] = senators[maximum]-1
            return (maximum,)
    else:
        senators[maximum] = senators[maximum]-1
        return (maximum,)

def solve(senators):
    senatorcount = 0
    numParties = 0
    for party in senators:
        if party > 0:
            numParties = numParties + 1
        senatorcount = senatorcount + party
    if len(senators) == 1:
        result = ""
        while senatorcount > 0:
            result = result + "A "
            senatorcount = senatorcount - 1
        return result.strip()
    elif numParties < 3:
        result = ""
        while senatorcount > 0:
            i = 0
            command = ""
            while len(command) < 2:
                if senators[i] != 0:
                    senators[i] = senators[i] - 1
                    command = command + toLetter(i)
                    senatorcount = senatorcount - 1
                i = i + 1
            result += command + " "
        return result.strip()
    else:
        result = ""
        while senatorcount > 0:
            removed = remove(senators, senatorcount)
            senatorcount = senatorcount - len(removed)
            if len(removed) == 1:
                result = result + toLetter(removed[0]) + " "
            else:
                result = result + toLetter(removed[0]) + toLetter(removed[1]) + " "
        return result.strip()

with open("1ALarge.in", "r") as filu:
    i = 0
    case = 1
    filu.readline()
    for line in filu:
        if i % 2:
            line = line.strip("\n")
            strings = line.split(" ")
            senators = []
            for string in strings:
                senators.append(int(string.strip()))
            print("Case #" + str(case) + ": "+solve(senators))
            case = case + 1
        i = i + 1
