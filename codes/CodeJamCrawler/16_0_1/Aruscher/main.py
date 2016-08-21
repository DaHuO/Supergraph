from collections import Counter

def main():
    t = int(input())
    for i in range (0,t):
        n = int(input())
        result = solve(n)
        print("Case #%d: %s"%(i+1,result))

def solve(n):
    if n == 0:
        return "INSOMNIA"
    else:
        i = 1
        count = Counter()
        while len(set(count)) != 10:
            #print("Update: "+str(n*i))
            count.update(str(n*i))
            i += 1
    return (i-1)*n



if __name__ == "__main__":
    main()
