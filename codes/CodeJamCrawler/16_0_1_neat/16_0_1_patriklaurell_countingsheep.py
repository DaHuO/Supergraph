import fileinput
import sys

def main():
    N = []
    for line in fileinput.input(sys.argv[1]):
        if not fileinput.isfirstline():
            line = line.rstrip()
            if line == '':
                continue
            N.append(int(line))
    solve(N)
    return

def solve(N):
    for i,n in enumerate(N):
        nums = set()
        currentn = n
        if n != 0:
            while len(nums) < 10:
                nums = nums | set(str(currentn))
                currentn = currentn + n
        print("Case #"+str(i+1)+": INSOMNIA" if n == 0 else "Case #"+str(i+1)+": "+str(currentn-n))
    return


if __name__=="__main__":
    main()
