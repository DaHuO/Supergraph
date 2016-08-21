__author__ = 'vitaly'

def f(n):
    ans = 0
    l = len(n)
    good = 0
    while n[l - good - 1] == '+':
        good += 1
        if good == l: break
    if good == l: return 0
    if good != 0:
        return f(n[:l-good])
    else:
        if n.find("+") == -1:
            return 1
        g = 0
        while n[g] == "+":
            g += 1
        n = n[0:g].replace("+", "-") + n[g:l - good]
        if g > 0 : ans += 1
        ans += 1
        n = n[::-1]
        s = ""
        #--+-
        #-+--
        for _ in n:
            if _ == "+":
                s += "-"
            else:
                s += "+"
        n = s
        return ans + f(n)

#res = open("res.txt", "w")
#inp = open("inp.txt", "r")
t = int(raw_input())
#t = int(inp.readline())
for i in range(t):
    #n = inp.readline()
    n = raw_input()
    #res.write("Case #{}: {}\n".format(i + 1, f(n.replace("\n",""))))
    print ("Case #{}: {}\n".format(i + 1, f(n)))