class Excercise1:

    def processTestCase(self, S):
        new_word = ""
        head = ""
        for letter in S:
            if new_word == "":
                new_word = letter
                head = letter
                continue
            if ord(letter) >= ord(head):
                head = letter
                new_word = letter + new_word
            else:
                new_word = new_word + letter
        return new_word

    def __init__(self):
        file = open('A-large.in', 'r')
        T = int(file.readline())
        testcase_number = 1
        for line in file:
            result = self.processTestCase(line.replace('\n',''))
            print("Case #%s: %s" % (testcase_number, result))
            testcase_number = testcase_number + 1


temp = Excercise1()
