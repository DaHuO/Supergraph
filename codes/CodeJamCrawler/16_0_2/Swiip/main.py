import argparse
parser = argparse.ArgumentParser()
parser.add_argument("path", help="path of the input file")
args = parser.parse_args()

def getPancakeState(upsideDowns, initialState):
    if (upsideDowns % 2 == 0):
        return initialState
    else:
        if initialState == "+":
            return "-"
        else:
            return "+"

if __name__ == "__main__":
    inputPath = args.path
    f = open(inputPath, 'r')
    f.readline()
    i = 1
    for line in f:
        stack = line.rstrip()
        upsideDowns = 0
        for pancake in reversed(stack):
            currentState = getPancakeState(upsideDowns, pancake)
            if currentState == "-":
                upsideDowns = upsideDowns + 1
        print("Case #" + str(i) + ": " + str(upsideDowns))
        i += 1
    f.close()
