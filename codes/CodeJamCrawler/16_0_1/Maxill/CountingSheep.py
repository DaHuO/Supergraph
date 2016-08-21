import argparse


def test_case(i, val):
    numerals = {str(k):0 for k in range(10)}

    print "Test case #%s: %s" % (i, val)

    if val == 0:
        return "INSOMNIA"

    mult = 1
    while (True):
        new = val * mult

        for c in str(new):
            numerals[c] += 1

        fail = False
        for count in [v for k,v in numerals.items()]:
            if count == 0:
                fail = True
                break

        if fail:
            mult += 1
            continue

        return new


def process(infile):
    with open("results", "w") as out:
        with open(infile) as f:
            contents = f.read().splitlines()

            spec = int(contents[0])
            cases = contents[1:]

            if spec != len(cases):
                print spec
                print len(cases)
                print "Specification mismatch with file content - aborting."
                exit(1)

            for i, val in enumerate(cases):
                result = test_case(i+1, int(val))
                print "Found answer: %s" % result
                out.write("Case #%s: %s\n" % (i + 1, result))



if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("infile", help="The file to process.")

    args = a.parse_args()
    process(args.infile)