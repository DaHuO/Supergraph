from math import*

def last(k):
    if k == 0:
        return "INSOMNIA"
    t = k
    cnt = [0] * 10
    while 1:
        for c in str(k):
            cnt[ord(c) - ord('0')] = 1
        ok = 1
        for i in range(10):
            if not cnt[i]:
                ok = 0
        if ok:
            return str(k)
        k += t

def main():
    fin = open("input.txt", "r")
    fout = open("output.txt", "w")
    n = int(fin.readline())
    for i in range(1, n + 1):
        print("Case #" + str(i) + ": " + last(int(fin.readline())), file = fout)
    fin.close()
    fout.close()

if __name__ == "__main__":
    main()