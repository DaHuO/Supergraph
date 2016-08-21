

def process(pancakes):
    count = 0
    #current = ""
    for i, ch in enumerate(pancakes[:-1]):
        if (pancakes[i] != pancakes[i+1]):
            #current = pancakes[i+1]
            count += 1
    if (pancakes[-1] == '-'):
        count += 1
    return count



if __name__ == "__main__":
    n = int(input().strip())
    for i in range(n):
        print("Case #" + str(i+1) + ": " + str(process(input().strip())))


