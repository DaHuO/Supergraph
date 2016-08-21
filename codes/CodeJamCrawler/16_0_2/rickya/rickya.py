from math import*

def solve(s):
    while s[-1] != "+" and s[-1] != "-":
        s = s[:-1:]
    n = len(s)
    t = [1 if i == "+" else 0 for i in s]
    dp = [[1e18 for i in range(2)] for j in range(n + 1)]
    dp[0][0] = 0
    dp[0][1] = 0
    for i in range(1, n + 1):
        if t[i - 1]:
            dp[i][1] = dp[i - 1][1]
            dp[i][0] = dp[i - 1][1] + 1
        else:
            dp[i][1] = dp[i - 1][0] + 1
            dp[i][0] = dp[i - 1][0]
    #print(dp)
    return str(dp[n][1])

def main():
    fin = open("input.txt", "r")
    fout = open("output.txt", "w")
    n = int(fin.readline())
    for i in range(1, n + 1):
        print("Case #" + str(i) + ": " + solve(fin.readline()), file = fout)
    fin.close()
    fout.close()

if __name__ == "__main__":
    main()