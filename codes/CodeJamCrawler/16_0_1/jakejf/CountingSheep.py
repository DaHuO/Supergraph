# Google Code Jam 2016
# Counting Sheep
# Jake Francis

def main():
    items = int(input())
    for x in range(1, items + 1):
        n = int(input())
        seen = [False] * 10
        i = 1
        output = "INSOMNIA"
        while (not checkSeen(seen)):
            if (n == 0): break
            output = str(n * i)
            for j in range(0, len(output)):
                seen[int(output[j])] = True
            i += 1
        print("Case #{}: {}".format(x, output))

def checkSeen(seen):
    for i in range (0, len(seen)):
        if seen[i] == False:
            return False
    return True    

main()
