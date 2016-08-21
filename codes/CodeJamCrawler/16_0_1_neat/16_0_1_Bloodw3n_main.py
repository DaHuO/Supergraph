class Number():
    def __init__(self, number):
        self.number = number
        self.parsedNumber = []
        self.counter = []
        self.lastSeen = 'INSOMNIA'
        self.newNumber = self.number


        self.interrater()

    def parser(self, givenNumber):
        number = givenNumber
        while (number // 10) > 0:
            last = number % 10
            number //= 10
            self.parsedNumber.append(last)
            if self.count(last):
                return 1

        self.parsedNumber.append(number)

        if self.count(number):
            return 1

    def count(self, last):
        if last not in self.counter:
            self.counter.append(last)

        if len(self.counter) == 10:
            self.lastSeen = self.newNumber
            return 1

    def interrater(self):
        if self.number == 0:
            return 0
        i = 1
        while True:
            self.newNumber = self.number * i
            if self.parser(self.newNumber):
                return 0
            i += 1


def main(t):

    for i in range(1, t+1):
        t = int(input())
        number = Number(t)
        print("Case #{}: {}".format(i, number.lastSeen))


main(int(input()))
