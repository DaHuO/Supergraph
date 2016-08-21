from base import GoogleJamBaseClass


class A(GoogleJamBaseClass):
    def read_case(self, input_file):
        return int(input_file.readline())

    def solve(self, case):
        case = int(case)
        if case == 0:
            return 'INSOMNIA'
        digits = {}
        i = 1
        number = 0
        while digits.__len__() < 10:
            number = i*case
            number_string = str(number)
            for ch in number_string:
                digits[ch] = True
            i += 1
        return number

A().run('A-large.in')
