import sys, os

def solve_pancake(n):
    print("solving: %s" % n)
    n=n.rstrip("+")

    steps = 0
    last = None
    for i in range(len(n)):
        cur = n[i]
        if   last is None and cur == "-":
            steps += 1
        elif last is None and cur == "+":
            steps += 1
        elif last is  "-" and cur == "+":
            steps += 1
        elif last is  "-" and cur == "-":
            pass
        elif last is  "+" and cur == "-":
            steps += 1
        elif last is  "+" and cur == "+":
            pass
        last = cur


    print("solved: %d steps for %s" % (steps, n))
    return steps


right = 0
wrong = []
def test_pancake(n, guess):
    global right, wrong
    soln = solve_pancake(n)
    if soln == guess:
        right += 1
    else:
        wrong += [(n, "guessed", soln, "but expected", guess)]

def contestMain():
    case = 1
    with open(sys.argv[1], "r") as ins:
        with open("outpankcake.txt", "w") as out:
            ins.readline()
            for line in ins:
                out.write("Case #%d: " % case)
                out.write(str(solve_pancake(line.rstrip("\n"))))
                out.write("\n")
                case += 1

def debugMain():

    test_pancake("+", 0)
    test_pancake("-", 1)

    test_pancake("--", 1)
    test_pancake("-+", 1)
    test_pancake("+-", 2)
    test_pancake("++", 0)

    test_pancake("---", 1)
    test_pancake("--+", 1)
    test_pancake("-+-", 3) 
    """ -+- +-+ -++ +++   -+- ++- --- +++ """
    test_pancake("+--", 2)
    test_pancake("-++", 1)
    test_pancake("++-", 2)
    test_pancake("+-+", 2)
    test_pancake("+++", 0)

    test_pancake("----", 1)
    test_pancake("---+", 1)
    test_pancake("--+-", 3)
    test_pancake("-+--", 3)
    test_pancake("+---", 2)

    test_pancake("--++", 1)
    test_pancake("-+-+", 3)
    test_pancake("+--+", 2)
    test_pancake("-++-", 3)
    test_pancake("+-+-", 4) 
    """ +-+- --+- +++- ---- ++++    +-+- -+-- ++-+ ---+ ++++ """
    test_pancake("++--", 2)
    test_pancake("-+++", 1)
    test_pancake("+-++", 2)
    test_pancake("++-+", 2)
    test_pancake("+++-", 2)
    test_pancake("++++", 0)

    test_pancake("-----", 1)
    test_pancake("----+", 1)
    test_pancake("---+-", 3)
    test_pancake("--+--", 3)
    test_pancake("-+---", 3)
    test_pancake("+----", 2)
    test_pancake("---++", 1)
    test_pancake("--+-+", 3) 
    """ --+-+ +++-+ ----+ +++++  --+-+ +-+++ --+++ +++++ """
    test_pancake("-+--+", 3) 
    """ -+--+ ++-++ +--++ ---++ ++++++   -+--+ ++--+ ----+ +++++ """
    test_pancake("+---+", 2)
    test_pancake("--++-", 3) 
    """ --++- ++++- ----- +++++ """
    test_pancake("-+-+-", 5) 
    """ 
     -+-+- ++-+- ---+- ++++- ----- +++++    
     -+-+- +-++- --++- +--++ ---++ +++++   
     -+-+- +-+-+ -+--+ ++--+ ----+ +++++
     -+-+- ++-+- -+--- ++--- ----- +++++
    """
    test_pancake("+--+-", 4)
    """
        +--+- ---+- ++++- ----- +++++
        +--+- +-++- --++- ++++- ...
        +--+- ++-+- ---+- ++++-
    """
    test_pancake("-++--", 3)
    test_pancake("+-+--", 4)
    test_pancake("++---", 2)
    test_pancake("--+++", 1)
    test_pancake("-+-++", 3)
    test_pancake("+--++", 2)
    test_pancake("-++-+", 3)
    test_pancake("+-+-+", 4)
    test_pancake("++--+", 2)
    test_pancake("-+++-", 3)
    test_pancake("+-++-", 4)
    test_pancake("+++--", 2)
    test_pancake("++++-", 2)
    test_pancake("+++-+", 2)
    test_pancake("++-++", 2)
    test_pancake("+-+++", 2)
    test_pancake("-++++", 1)
    test_pancake("+++++", 0)

    print(right)
    print(wrong)



if __name__ == "__main__":
    #debugMain()
    #printdebug = False
    #main1()
    contestMain()