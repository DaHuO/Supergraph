f = open("in.txt", "r")
g = open("out.txt", "w")

t = int(f.readline())

for tc in range (1, t + 1):
    ans = 0
    stack = str(f.readline())
    stack = stack[::-1]
    while (True):
        tmp = ""
        flag = False
        for s in stack:
            if flag:
                if s == '+':
                    tmp += '-'
                else:
                    tmp += '+'
            else:
                if s == '-':
                    flag = True
                    
                tmp += '+'
                
        if flag:
            ans += 1
            stack = tmp
        else:
            break
            
    g.write("Case #{}: {}\n".format(tc, ans))    

f.close()
g.close()