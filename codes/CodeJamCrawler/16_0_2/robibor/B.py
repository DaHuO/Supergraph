
def simplify(str):
    newstr=str[0]
    i=1
    while i < len(str):
        if str[i] != newstr[-1]:
            newstr+=str[i]
        i+=1
    return newstr


def solve(str):
    str = simplify(str)
    lenstr=len(str)
    if str[-1] == '+':
        return (lenstr-1)
    else:
        return lenstr


def read():
    with open("B-large.in", "r") as filein:
        with open("Bout_large.txt", "w") as fileout:
            lines = filein.readlines()
            ii=1
            for line in lines[1:]:
                out=solve(line.strip())
                mystr = "Case #" + str(ii) + ": " + str(out) + "\n"
                ii += 1
                fileout.write(mystr)

if __name__ == '__main__':
    read()
