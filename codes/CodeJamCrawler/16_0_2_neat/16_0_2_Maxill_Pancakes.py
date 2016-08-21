import argparse

PANCAKE_HAPPY = "+"
PANCAKE_BLANK = "-"

def test_case(i, stack):
    print "Working on test case #%s: %s" % (i, "".join(stack))

    finished = True if len(filter(lambda x: x == PANCAKE_BLANK, stack)) == 0 else False
    iter = 0
    while not finished:
        start_cake = stack[0]

        i = 1
        changed = False
        while i < len(stack):
            if stack[i] != start_cake:
                new_cake = PANCAKE_BLANK if start_cake == PANCAKE_HAPPY else PANCAKE_HAPPY
                new_stack = [new_cake] * i + stack[i:]
                changed = True
                break

            i += 1

        if not changed:
            new_cake = PANCAKE_BLANK if start_cake == PANCAKE_HAPPY else PANCAKE_HAPPY
            new_stack = [new_cake] * i + stack[i:]

        iter += 1
        stack = new_stack

        print "Iteration %s: %s" % (iter, "".join(new_stack))

        finished = True if len(filter(lambda x: x == PANCAKE_BLANK, stack)) == 0 else False

    return iter

def process(infile):
    with open("results_pancakes", "w") as out:
        with open(infile) as f:
            contents = f.read().splitlines()

            spec = int(contents[0])
            cases = contents[1:]

            if spec != len(cases):
                print spec
                print len(cases)
                print "Specification mismatch with file content - aborting."
                exit(1)

            for i, stack in enumerate(cases, start=1):
                result = test_case(i, list(stack))
                print "Found answer: %s" % result
                out.write("Case #%s: %s\n" % (i, result))



if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("infile", help="The file to process.")

    args = a.parse_args()
    process(args.infile)