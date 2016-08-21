import fileinput
import sys

def main():
    l = []
    for line in fileinput.input(sys.argv[1]):
        if not fileinput.isfirstline():
            l.append(line.rstrip())

    solve(l)
    return

def solve(N):
    for index, s in enumerate(N):
        count = 0
        while '-' in s:
            i = s.find('+' if s[0]=='-' else '-')
            if i != -1:
                s = "".join(['+' if s[0]=='-' else '-' for x in range(i)]) + s[i:]
            else:
                if s[0] == '-':
                    count = count + 1
                break
            count = count + 1
            if count == 10:
                break
        print("Case #"+str(index+1)+": "+str(count))

if __name__=="__main__":
    main()

