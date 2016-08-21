def remove(s):
    flag = True
    new = ''
    for it in s:
        if not flag:
            new += it
        elif it=='-' and flag:
            flag = False
            new += it
    return new[::-1]

def rev(s):
    s = s[::-1]
    new = ''
    for it in s:
        if it=='+':
            new += '-'
        else:
            new += '+'
    return new

def solve(st):
    global answer
    st_rev = st[::-1]
    st = remove(st_rev)
    if len(st)==0:
        return 
    else:
        if st[0]=='-':
            answer += 1
            st = rev(st)
            solve(st)
        else:
            flag = True
            new = ''
            answer += 1
            for it in st:
                if it=='+' and flag:
                    new += '-'
                elif it=='-' and flag:
                    new += it
                    flag = False
                elif flag==False:
                    new += it
            st = new[:]
            answer += 1
            st = rev(st)
            solve(st)

for cases in range(input()):
    st = raw_input()
    answer = 0
    solve(st)
    print "Case #"+ str(cases+1) + ": " + str(answer)
