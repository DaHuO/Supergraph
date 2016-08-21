from sys import stdin

def main():
    a = int(stdin.readline().strip())
    for j in range(a):
        cad = stdin.readline().strip()
        temp = cad[0] ; cont = 0
        for i in range(1,len(cad)):
            if cad[i] != temp:
                temp = cad[i]
                cont += 1
        if temp == '-': cont += 1
        print("Case #{0}: {1}".format(j+1, cont))
main()
