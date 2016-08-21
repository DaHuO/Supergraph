import sys
sys.setrecursionlimit(10**6)
def recurse(tail, head="", ans=set()):
    if not tail:
        ans.add(head)
        return ans
    else:
        next_letter = tail[0]
        if head and ord(next_letter) >= ord(head[0]):
            return recurse(tail[1:], next_letter + head,ans)
        else:
            return recurse(tail[1:], head +next_letter ,ans)
def solve(s):
    return sorted(recurse(s, "", set()))[-1]
def main():
    n_cases = int(input())
    for case in range(1,n_cases+1):
        s = input()
        print("Case #{}: {}".format(case,solve(s)))

if __name__ == '__main__':
    main()
