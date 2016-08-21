def calc(file):
    s = list(file.readline().split()[0])
    last = 'x'
    ans = 0
    for i in s:
        if i == '+':
            last = i
            continue
        if last == '+':
            last = i
            ans += 2
            continue
        if last == 'x':
            last = i
            ans += 1
            continue
    return ans

def main():
    file = open("input.txt")
    fl_o = open("output.txt", 'w')
    T = int(file.readline())
    for t in range(T):
        ans = calc(file)
        fl_o.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
    fl_o.close()

main()