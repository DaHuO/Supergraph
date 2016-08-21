from sys import stdin

temp = list()

def create():
    global temp
    temp = [ False for i in range(10) ]

def solve(cad):
    global temp
    if cad == '0':
        ans = "INSOMNIA"
    else:
        create()
        a = 1
        while False in temp:
            for i in str(int(cad)*a):
                temp[int(i)] = True
            a+=1
        ans = str(int(cad)*(a-1))
    return ans

def main():
    a = int(stdin.readline())
    for i in range(a):
        print("Case #{0}: {1}".format(str(i+1), solve(stdin.readline().strip())))
main()
