input_S = []
f = open("B-large.in", "r")
g = open("B-largeout.txt", "w")
for line in f:
    input_S.append(line)
output_N = []

def flips(s):
    h = 0
    while s.rfind("-") != -1:
        x = s.rfind("-")
        for y in range(0,x+1):
            if s[y] == "+":
                s = s[:y] + "-" + s[y+1:]
            else:
                if s[y] == "-":
                    s = s[:y] + "+" + s[y+1:]
        h += 1
    return h 



for x in range(1,len(input_S)):
    g.write("Case #%s: %s\n" %(x, flips(input_S[x])))

f.close()
g.close()
