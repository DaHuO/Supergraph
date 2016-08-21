class CountingSheeps:

    def isComplete(self, numbers):
        if None in numbers:
            return False
        else:
            return True

    def analyzeNumbers(self, value, numbers):
        value_array = map(int,str(value))
        for number in value_array:
            numbers[number] = 1
        return numbers

    def processTestCase(self, N):
        if N == 0:
            return "INSOMNIA"
        numbers = [None] * 10
        multiplier = 1
        value = None
        while self.isComplete(numbers) is False:
            value = multiplier * N
            numbers = self.analyzeNumbers(value, numbers)
            multiplier = multiplier + 1
        return value

    def __init__(self):
        file = open('A-large.in', 'r')
        T = int(file.readline())
        testcase_number = 1
        for line in file:
            result = self.processTestCase(int(line))
            print("Case #%s: %s" % (testcase_number, result))
            testcase_number = testcase_number + 1


Bleatrix  = CountingSheeps()
