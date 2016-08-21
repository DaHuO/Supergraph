from base import GoogleJamBaseClass


class D(GoogleJamBaseClass):
    def read_case(self, input_file):
        line = input_file.readline().strip()
        length, complexity, positions = line.split(' ')
        return int(length)

    def solve(self, case):
        positions = range(1, case + 1)
        return ' '.join([str(i) for i in positions])


D().run('D-small-attempt0.in')
