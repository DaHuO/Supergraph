
def countTillAsleep(n):
    if n == 0: return "INSOMNIA"
    seen = set()
    num = 0
    while len(seen) < 10:
        num += n
        for x in str(num):
            seen.add(x)
        
    return num

def main():
    n = int(input())
    for i in range(n):
        x = int(input())
        print("Case #%s:" %(i+1), countTillAsleep(x))

main()
