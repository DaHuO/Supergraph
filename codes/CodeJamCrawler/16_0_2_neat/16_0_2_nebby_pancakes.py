import sys
inputs = sys.stdin.readline()
for x in range(int(inputs)):
    pancakes = sys.stdin.readline()
    reverse_pancakes = pancakes[::-1]
    flips = 0
    first_unhappy = reverse_pancakes.find('-')
    if(first_unhappy != -1):
        search_reverse_pancakes = reverse_pancakes[first_unhappy:]
        prev = '-'
        flips += 1
        for pancake in search_reverse_pancakes:
            if(pancake != prev):
                flips += 1
                prev = pancake
    print('CASE #' + str((x+1)) + ': ' + str(flips))
