def senate(N,list):
    res = ""
    if len(list)%2 == 1:
        s = list.index(max(list))
        res = res + chr(s)
        list[s] -= 1
    else:
        s = list.index(max(list))
        res = res + chr(s)
        list[s] -= 1
        s = list.index(max(list))
        res = res + chr(s)
        list[s] -= 1
    while max(list) != 0:
        s = list.index(max(list))
        res = res + " " + chr(s)
        list[s] -= 1
        s = list.index(max(list))
        res = res + " " + chr(s)
        list[s] -= 1
    return(res)

def main():
    f = open("input.txt", 'r')
    r = open("output.txt", 'w')
    readline(f)
    N = 0
    senators = []
    count = 0
    case = 0
    for line in f:
        if count%2 == 0:
            N = int(line)
        else:
            list = line.split()
            case += 1
            res.write(senate(N,list) + "\n")

            