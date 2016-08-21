import sys

def flip(l):
    l = l[::-1]
    for i in range(len(l)):
        if l[i] == "+":
            l[i] = "-"
        else:
            l[i] = "+"
    return l

def solution(s):
    #return flip times
    l = list(s)
    last = len(s)-1
    res = 0
    while '-' in l:
        i=0
        while i<last and l[i+1]==l[i]:
            i+=1
        l[:i+1] = flip(l[:i+1])
        res+=1
    return res




def main():
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    for i in range(1,len(lines)):
        res = solution(lines[i])
        print('Case #%d: %d' % (i,res))



if __name__ == '__main__':
    main()