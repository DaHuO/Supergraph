
class CountingSleep(object):

    def __init__(self, chosen_number):
        self.chosen_number = chosen_number
        self.counted_digits = []

    def process_chosen_number(self, current_number):
        multiple_of_chosen_number = current_number + self.chosen_number
        if current_number == multiple_of_chosen_number:
            return "INSOMNIA"
        number = str(multiple_of_chosen_number)
        num_as_string = str(number)
        for digit in num_as_string:
            if digit not in self.counted_digits:
                self.counted_digits.append(digit)

        if len(self.counted_digits) == 10:
            return multiple_of_chosen_number
        else:
            return self.process_chosen_number(multiple_of_chosen_number)


if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = int(raw_input())
        result = CountingSleep(n).process_chosen_number(0)
        print "Case #{}: {}".format(i, result)
