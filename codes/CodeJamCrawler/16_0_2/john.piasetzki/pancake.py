"""Pancakes"""
import fileinput

def main():
    """Main Method"""
    handler = fileinput.input()
    appearences = int(handler.readline())
    for case in range(1, appearences+1):
        stack = handler.readline().strip()
        last = stack[0]
        flips = 0
        for pancake in str(stack)[1:]:
            if pancake == last:
                continue
            else:
                flips += 1
            last = pancake

        if last == '-':
            flips += 1

        print "Case #{0}: {1}".format(case, flips)

if __name__ == "__main__":
    main()
