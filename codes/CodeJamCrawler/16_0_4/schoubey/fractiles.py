import sys
std_in = sys.stdin

def main():
    T = int(std_in.readline())
    for i in range(T):
        input_line = std_in.readline()
        input_line.strip()
        ilist = input_line.split(' ',3)
        ilist = list(map(int, ilist))
        K = ilist[0]
        C = ilist[1]
        S = ilist[2]
        print("Case #" + str(i+1) + ":", end = '')
        for i in range(1,S + 1):
            print(" " + str(i), end = '')
        print()
main()
