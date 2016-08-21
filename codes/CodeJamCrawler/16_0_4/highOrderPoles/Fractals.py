import numpy as np
from collections import Counter
import itertools

class Fractals:
    def readLimits(self):
        # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
        # This is all you need for most Google Code Jam problems.
        self.cases = []
        self.numCases = 0

        self.numCases = int(raw_input())  # read a line with a single integer
        for i in xrange(1, self.numCases + 1):
            line = [int(s) for s in raw_input().split(" ")]
            self.cases.append(line)

    def printOne(self, results):
        for i in xrange(len(results)):
            n = results[i]
            print "Case #{}: {}".format(i + 1, n)

    def run(self):
        self.results = []
        self.readLimits()
        for case in self.cases:
            size, complexity, searchLim = case
            self.process(size, complexity, searchLim)
        self.printOne(self.results)

    def process(self, size, complexity, searchLim):
        # print size, complexity, searchLim

        startingTiles = self.generateStartingComboPower2(size)

        # print "Starting tile lenghts: ", len(startingTiles)

        finalTiles = []
        for tile in startingTiles:
            finalTile = self.getNextGeneration(tile, complexity, tile, size)
            finalTiles.append(finalTile)

        # print size, searchLim, startingTiles, "->", finalTiles

        if searchLim == size:
            obviousResult = " ".join(str(tile[0]) for tile in finalTiles)
            self.results.append(obviousResult)
        else:
            self.results.append(self.searchGold(finalTiles, size, searchLim))

    def searchGold(self, finalTiles, size, searchLim):
        result = 0
        steps = 0

        if len(finalTiles) == 1:
            result = 1  # Trivial case
        else:
            # 1) Find least common tile number, this means other tiles have gold in this location
            result = []

            while len(finalTiles) > 1 and steps < searchLim:
                collapsed = [item for sublist in finalTiles for item in sublist]
                # print collapsed
                counts = Counter(collapsed)
                # print counts

                leastCommonTile, freq = counts.most_common()[-1]
                # print leastCommonTile

                # Check for zeros
                checkZero = 1
                while checkZero < max(collapsed):
                    if counts[checkZero] == 0:
                        leastCommonTile = checkZero
                        break
                    checkZero += 1

                result.append(leastCommonTile)
                # print "Least bit in counter:", leastCommonTile

                newTiles = []
                for tile in finalTiles:
                    if leastCommonTile in tile:
                        newTiles.append(tile)
                    else:
                        leftOverTile = tile[0]

                # print newTiles
                finalTiles = newTiles

                steps += 1

            # 2) Pick a different tile
            if (len(finalTiles) == 1):
                result.append(leftOverTile)
                result = " ".join(str(step) for step in result)
                steps += 1
                if (steps > searchLim):
                    result = "IMPOSSIBLE"
            # Unless hidden Golds knocks out all of them
            elif len(finalTiles) == 0:
                result = " ".join(str(step) for step in result)

        return result

    def getNextGeneration(self, tile, complexity, startingTile, size):
        newTile = []

        # print tile, complexity, size
        for i in tile:
            for j in startingTile:
                newLead = (i - 1) * size + j
                newTile.append(newLead)

        if complexity > 2:
            newTile = self.getNextGeneration(newTile, complexity - 1, startingTile, size)
        if complexity == 1:  # nothing changes here
            newTile = tile

        return newTile



    def generateStartingComboPower2(self, size):
        # maxLead = np.power(2, size)
        possibleCombos = []

        # for lead in range(1, maxLead - 1, 1):
        inputLead = 1
        while inputLead < size + 1:
            leadArray = [inputLead]
            inputLead += 1
            possibleCombos.append(leadArray)
            # index = 0
            # while index < size:
            #     leftMostDigit = lead % 2
            #     leadArray[index] = leftMostDigit
            #     lead = int(np.floor(lead / 2))
            #     index += 1
            # indices = [i + 1 for i, x in enumerate(leadArray) if x == 1]
            # possibleCombos.append(indices)
            # inputLead = 2 * inputLead

        return possibleCombos


def main():
    q4 = Fractals()
    q4.run()


if  __name__ =='__main__':
    main()
