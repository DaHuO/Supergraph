import sys

def countsheeps(N):
    if (N == 0):
        return "INSOMNIA"
    k = 0
    found = set()
    while len(found) != 10:
        k += 1
        for char in str(k*N):
            found.add(char)
    return str(k*N)

if __name__ == "__main__":
    case = 1
    filename = sys.argv[1]
    file = open(filename,'r')
    out = open("Sheep_Output.txt",'w')
    file.readline() #that first line is useless
    for lineremaining in file:
        out.writelines("Case #{}: {}\n".format(case,countsheeps(int(lineremaining.strip()))))
        case += 1

