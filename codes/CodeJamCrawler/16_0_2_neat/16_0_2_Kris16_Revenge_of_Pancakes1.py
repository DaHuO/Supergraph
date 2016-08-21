#Revenge of the Pancakes.
in_f = open("B-large.in")
lines = [i.strip("\n") for i in in_f.readlines()]
in_f.close()
tcs = int(lines[0])

def rev_str(s):
    rs = ""
    for i in range(len(s)):
        if s[i] == "+":
            rs = rs + "-"
        else:
            rs = rs + "+"
    return rs

with open("output_large.ot", "w") as out_f:
    for i in range(1, tcs+1):
        if lines[i].count("+") == len(lines[i]):
            out_f.write("Case #%s: %s\n"%(i,0))
        else:
            if lines[i].count("-") == len(lines[i]):
                out_f.write("Case #%s: %s\n"%(i,1))
            else:
                cnt = 0
                for j in range(len(lines[i])-1,-1,-1):
                    if lines[i][j] == '-':
                        lines[i] = rev_str(lines[i][:j]) + "+" + lines[i][j+1:] 
                        cnt += 1
                    if lines[i][:j-1].count("-") == len(lines[i][:j-1]):
                        cnt += 1
                        break
                out_f.write("Case #%s: %s\n"%(i,cnt))
