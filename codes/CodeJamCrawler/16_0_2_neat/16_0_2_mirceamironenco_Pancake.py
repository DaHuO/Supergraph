def number_of_flips(pancakes):
    moves = 0
    for i in range(len(pancakes)):
        if pancakes[i] == "-":
            j = i
            while j < len(pancakes) and pancakes[j] == "-":
                j += 1
            x = i - 1
            while x >= 0 and pancakes[x] == "+":
                x -= 1
            if i-1 >= 0:
                for a in range(i-1,x,-1):
                    pancakes[a] = "-"
                moves += 1
            for b in range(x+1,j):
                pancakes[b] = "+"
            moves += 1

    return moves

if __name__ == "__main__":
    test_cases = int(input().strip())
    for i in range(test_cases):
        pancakes = str(input().strip())
        moves = number_of_flips(list(pancakes))
        print("Case #{}: {}".format(i+1,moves))
