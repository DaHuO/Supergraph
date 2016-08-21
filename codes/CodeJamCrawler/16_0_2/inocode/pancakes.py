from sys import stdin

# S is the start state
# M :: S -> [S]
# G :: S -> boolean
# Returns a path (a list of S) from start to goal
def solve(S,M,G):

    seenStates = {S}

    paths = [[S]]
    nextPaths = []

    while True:
        for path in paths:
            lastS = path[len(path)-1]
            if G(lastS):
                return path
            else:
                nextStates = filter( lambda s: not s in seenStates, M(lastS))
                for nextState in nextStates:
                    seenStates.add(nextState)
                    nextPaths.append( path + [nextState] )

        if len(nextPaths) == 0:
            return None

        paths = nextPaths
        nextPaths = []

def flip(pancake):
    if pancake == "-":
        return "+"
    elif pancake == "+":
        return "-"
    else:
        return "?"

def maneuver(S,i):

    # print("maneuver %s %d" % (S,i))

    top = S[:i+1]
    bottom = S[i+1:]

    revTop = list(map(flip,top))
    revTop.reverse()
    revTop = "".join(revTop)

    return revTop + bottom

def move(S):
    return [ maneuver(S,i) for i in range(0,len(S)) ]

def goal(S):
    return all(map(lambda p: p == "+", S))

def main():

    T = int(stdin.readline())

    for t in range(0,T):

        S = stdin.readline().strip()
        path = solve(S,move,goal)

        answer = len(path)-1 if not path == None else "None"

        print("Case #%d: %s" % (t+1,answer))

if __name__ == "__main__":
    main()
