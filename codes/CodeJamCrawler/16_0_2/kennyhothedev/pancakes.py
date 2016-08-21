def revengePancakes(pancakes):
    pancakes = list(pancakes)

    if allPluses(pancakes):
        return 0

    else:
        falseIndex = len(pancakes)-1

        for n in range(len(pancakes)-1 , -1, -1):

            if pancakes[n] == "-":
                falseIndex = falseIndex - n
                break

        for n in range(len(pancakes) - falseIndex -1, -1, -1):
            if pancakes[n] == "+":
                pancakes[n] = "-"
            else:
                pancakes[n] = "+"
        return 1 + revengePancakes(pancakes)

def allPluses(pancakes):
    for i in pancakes:
        if i != "+":
            return False
    return True

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  pancakes = raw_input() # read a list of integers, 2 in this case
  print  "Case #{}: {}".format(i,revengePancakes(pancakes))
  # check out .format's specification for more formatting options