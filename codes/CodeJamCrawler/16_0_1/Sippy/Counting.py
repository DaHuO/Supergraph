def calc(file):
    n = int(file.readline())
    if n==0: return "INSOMNIA"
    arr = [0]*10
    ans = 0
    while True:
        if sum(arr) == 10: return ans
        ans += n
        k = ans
        while k > 0:
            d = k%10
            k = k/10
            arr[d] = 1

def main():
    file = open("input.txt")
    fl_o = open("output.txt", 'w')
    T = int(file.readline())
    for t in range(T):
        ans = calc(file)
        fl_o.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
    fl_o.close()

main()