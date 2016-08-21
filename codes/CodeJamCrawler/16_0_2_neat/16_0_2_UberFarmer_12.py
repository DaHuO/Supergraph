from sys import stdin

def main():
    num_cases = int(stdin.readline())
    for case in range(1, num_cases + 1):
        pancakes = stdin.readline().strip()
        if pancakes[-1] == '-':
            flips = 1
        else:
            flips = 0
        for i in range(len(pancakes) - 1):
            if pancakes[i] != pancakes[i + 1]:
                flips += 1
        print "Case #{}: {}".format(case, flips)

if __name__ == "__main__":
    main()
