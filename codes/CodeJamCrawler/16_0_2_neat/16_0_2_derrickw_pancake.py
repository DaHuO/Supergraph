def pancakeFlips(pancakes):
    flips = 0

    for i in range(len(pancakes)-1,-1,-1):
        if pancakes[i] == "+":
            continue
        else:
            if pancakes[0] == "-":
                flips += 1
                pancakes = flipPancakes(i,pancakes)
            else:
                flips += 2
                pancakes = flipPancakes(otherPlus(i,pancakes),pancakes)
                pancakes = flipPancakes(i,pancakes)
    return flips, pancakes


def otherPlus(stop, pancakes):

    for i in range(stop,-1,-1):
        if pancakes[i] == "+":
            return i


def flipPancakes(stop, pancakes):

    for i in range(stop // 2 + 1):
        if i == stop-i:
            pancakes[i] = flip(pancakes[i])
        else:
            pancakes[i] = flip(pancakes[i])
            pancakes[stop-i] = flip(pancakes[stop-i])
    return pancakes


def flip(pancake):
    if pancake == "+":
        pancake = "-"
    else:
        pancake = "+"
    return pancake


def main():

    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        flips, pancakes = pancakeFlips(list(input()))
        print ("Case #{}: {}".format(i, flips))

if __name__=='__main__':
    main()