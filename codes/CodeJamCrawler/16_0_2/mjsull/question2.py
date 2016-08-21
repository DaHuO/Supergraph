import sys
import string
transtab = string.maketrans('-+', '+-')
out_file = open(sys.argv[2], 'w')
with open(sys.argv[1]) as in_file:
    num_cases = int(in_file.readline())
    for i in range(1, num_cases + 1):
        pancakes = in_file.readline().rstrip()
        flips = 0
        while '-' in pancakes:
            flips += 1
            first_neg = pancakes.find('-')
            if first_neg == 0:
                last_neg = pancakes.rfind('-')
                unflipped = pancakes[last_neg+1:]
                flipped = pancakes[:last_neg+1]
                flipped = flipped[::-1].translate(transtab)
                pancakes = flipped + unflipped
            else:
                unflipped = pancakes[first_neg:]
                flipped = pancakes[:first_neg]
                flipped = flipped[::-1].translate(transtab)
                pancakes = flipped + unflipped
        out_file.write('Case #' + str(i) + ': ' + str(flips) + '\n')


