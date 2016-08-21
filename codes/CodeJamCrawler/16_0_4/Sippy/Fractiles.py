def calc(file):
    k, c, s = map(int, file.readline().split())
    arr = [1]*s
    for i in range(s):
        arr[i] = i+1


def main():
    file = open("input.txt")
    fl_o = open("output.txt", 'w')
    T = int(file.readline())
    for t in range(T):
        k, c, s = map(int, file.readline().split())
        fl_o.write("Case #" + str(t+1) + ": ")
        for i in range(s):
            fl_o.write(str(i+1) + " ")
        fl_o.write("\n")
    fl_o.close()

main()