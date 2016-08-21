
class TestCase:
    def __init__(self, caseIndex):
        self.caseIndex = caseIndex

    def parseInput(self):
        self.S = raw_input()
        self.lastWord = ""

    def run(self):
        for character in self.S:
            if len(self.lastWord) == 0:
                self.lastWord += character
            elif ord(character) >= ord(self.lastWord[0]):
                self.lastWord = character + self.lastWord
            else:
                self.lastWord += character

    def generateOutput(self):
        print "Case #%d: %s" % (self.caseIndex, self.lastWord)

for caseIndex in range(1, int(raw_input()) + 1):
    testCase = TestCase(caseIndex)
    testCase.parseInput()
    testCase.run()
    testCase.generateOutput()
