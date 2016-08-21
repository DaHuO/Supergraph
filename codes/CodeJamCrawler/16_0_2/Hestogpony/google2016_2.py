import math

def flip(orderedPancakes, number):
    newOrderedPancakes = (orderedPancakes[0: number]).replace("+", "minus").replace("-", "plus"). \
        replace("plus", "+").replace("minus", "-")
    return newOrderedPancakes[::-1] + orderedPancakes[number:]

def correctlyTurned(pancakes):
    for s in pancakes:
        if s == "+":
            continue
        else:
            return False
    return True

def countPlusAndMinus(pancakes):
    plus = 0
    minus = 0
    for i in range (0, len(pancakes)):
        if pancakes[i] == "+":
            plus += 1
        else:
            minus += 1
    return plus, minus

def allMinus(pancakes):
    plus, minus = countPlusAndMinus(pancakes)
    return len(pancakes) == minus

inputFile = open("B-large.in", "r")
# inputFile = open("input.in", "r")
outputFile = open("output.out", "w")

n = inputFile.next()
print n

for j in range(0, int(n)):
    pancakes = inputFile.next()
    pancakes = str.strip(pancakes, "\n")
    flips = 0
    lastFlippedIndex = 0
    while not correctlyTurned(pancakes):
        first = pancakes[0]
        print "Working on: " + pancakes
        for i in range(0, len(pancakes)):
            if allMinus(pancakes):
                    print "All minusses!"
                    pancakes = flip(pancakes, len(pancakes))
                    flips += 1
                    print "Flips: " + str(flips)
                    break
            elif len(pancakes) == 1:
                if pancakes[0] == "-":
                    pancakes = flip(pancakes, len(pancakes))
                    flips += 1
                    break
                else:
                    break
            elif pancakes[i] == first:
                continue
            else:
                print "Flipping " + pancakes + " at index: " + str(i)
                pancakes = flip(pancakes, i)
                print "After flip: " + pancakes
                flips += 1
                print "Flips: " + str(flips)
                break
    outputFile.write("Case #" + str(j+1) + ": " + str(flips) + "\n")
#
# for j in range(0, int(n)):
#     pancakes = inputFile.next()
#     pancakes = str.strip(pancakes, "\n")
#     flips = 0
#     while not correctlyTurned(pancakes):
#         max = -999
#         indexToFlip = 0
#         print "Working on: " + pancakes
#         for i in range(0, len(pancakes)):
#             plus, minus = countPlusAndMinus(flip(pancakes, i + 1))
#             difference = plus - minus
#             print "Index: " + str(i + 1)
#             print "Plusses: " + str(plus) + " minusses: " + str(minus) + " Difference: " + str(difference)
#             if difference > max and not len(pancakes) == i + 1:
#                 max = difference
#                 indexToFlip = i + 1
#         print "Flipping " + pancakes + " at index: " + str(indexToFlip)
#         pancakes = flip(pancakes, indexToFlip)
#         flips += 1
#         print "Flips: " + str(flips)
#         if allMinus(pancakes):
#             pancakes = flip(pancakes, len(pancakes))
#             flips += 1
#     outputFile.write("Case #" + str(j+1) + ": " + str(flips) + "\n")