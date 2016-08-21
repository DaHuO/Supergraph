def main():
    with open("pancakes.txt") as data:
        caseno = 0
        cases = data.readline()
        for S in data.readlines():
            S = list(S.strip())
            caseno += 1
            counter = 0
            while not done(S):
                flip(S)
                counter += 1
            print("Case #{}: {}".format(caseno, counter))

def done(pancakes):
    for i in pancakes:
        if i != "+":
            return False
    return True

def flip(pancakes):
    currentsym = pancakes[0]
    if currentsym == "+":
        opposite = "-"
    else:
        opposite = "+"
    counter = 0
    for i in pancakes:
        if i == currentsym:
            pancakes[counter] = opposite
            counter += 1
        else:
            assert i == opposite
            break

main()
