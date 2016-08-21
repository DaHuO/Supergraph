import sys

def flipsearch(pancakes):
    if len(pancakes) == 0:
        return 0
    count = numberOfSegments(pancakes)
    if pancakes[-1] == '+':
        return count - 1
    else:
        return count


def numberOfSegments(string):
    last = string[0]
    count = 1
    for char in string:
        if char != last:
            count += 1
            last = char
    return count

if __name__ == "__main__":
    case = 1
    filename = sys.argv[1]
    file = open(filename,'r')
    out = open("Flippy_Output.txt",'w')
    file.readline() #that first line is useless
    for lineremaining in file:
        out.writelines("Case #{}: {}\n".format(case,flipsearch(lineremaining.strip())))
        case += 1

