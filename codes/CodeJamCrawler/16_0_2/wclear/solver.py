def solve(n):
    # Just need to know the number of flips which is given
    # as the number of clusters of pancake orientations 
    # plus 1 if the last is an unhappy pancake
    previous = None
    flipCount = 0
    for char in n:
        if previous is not None and previous != char:
            flipCount += 1
        previous = char

    if n[-1:] == "-":
        flipCount += 1

    return str(flipCount)