def flip1(string):
    split = list(string)
    for k in range(len(string)):
        if split[k] == '+':
            split[k] = '-'
        else:
            split[k] = '+'
        "".join(split)
    return split

output = open("B-large.out", "w")
with open("B-large.in") as f:
    T = f.readline()
    T = int(T)
    for j in range(T):
        s = f.readline()
        s = s.replace('\n', '')
        flip = 0
        i = len(s)-2
        if len(s) == 1:
            i = 0
        while i >= 0:
            if not len(s) == 1:
                if not s[i] == s[i+1]:
                    split = s[0:i+1]
                    if s[i] == "+":
                        flip += 1
                        s = flip1(split)
            if i == 0 or len(s) == 1:
                if s[i] == "-":
                        flip += 1
            i -= 1
        output.write("Case #"+str(j+1)+": "+str(flip)+"\n")






