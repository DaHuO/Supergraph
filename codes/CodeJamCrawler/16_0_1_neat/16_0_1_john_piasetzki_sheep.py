"""The Price is Correct Challenge"""
import fileinput

def main():
    """Main Method"""
    handler = fileinput.input()
    appearences = int(handler.readline())
    cases = []
    for case in range(1, appearences+1):
        number = int(handler.readline())
        if number == 0:
            cases.append('INSOMNIA')
        else:
            seen = set()
            i = 1
            while len(seen) < 10:
                last = i * number
                for digit in str(last):
                    seen.add(digit)
                i += 1
            cases.append(last)

    for case, number in enumerate(cases, start=1):
        print "Case #{0}: {1}".format(case, number)

if __name__ == "__main__":
    main()
