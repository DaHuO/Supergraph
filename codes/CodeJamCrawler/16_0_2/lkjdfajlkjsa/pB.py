
def numFlips(pancakes):
    flips = 0
    should_be_happy_side = True
    for pancake in pancakes:
        if pancake != should_be_happy_side:
            flips += 1
            should_be_happy_side = not should_be_happy_side
    return flips


for t in range(1, int(input()) + 1):
    pancakes = reversed(tuple(pancake == '+' for pancake in input()))
    print("Case #{}: {}".format(t, numFlips(pancakes)))
