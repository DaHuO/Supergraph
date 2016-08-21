class Pancakes:

    def flip(self, pancakes_stack):
        flipped_stack = ""
        # Reversing order and change face.
        for pancake in pancakes_stack:
            if pancake == '-':
                flipped_stack = '+' + flipped_stack
            else:
                flipped_stack = '-' + flipped_stack
        return flipped_stack

    def processTestCase(self, line):
        flips = 0
        last_index = len(line)
        if '-' not in line:
            return flips
        while '-' in line:
            for index, face in enumerate(line):
                if face == '+' and line[0] == '+':
                    if index + 1 == last_index:
                        return
                    continue
                if face == '-' and line[0] == '+':
                    tmp_line = self.flip(line[:index])
                    line = tmp_line + line[index:]
                    flips = flips + 1
                    break
                if face == '-' and line[0] == '-':
                    if index + 1 == last_index:
                        line = self.flip(line)
                        flips = flips + 1
                        break
                    continue
                if face == '+' and line[0] == '-':
                    tmp_line = self.flip(line[:index])
                    line = tmp_line + line[index:]
                    flips = flips + 1
                    break
        return flips

    def __init__(self):
        file = open('B-large.in', 'r')
        T = int(file.readline())
        testcase_number = 1
        for line in file:
            result = self.processTestCase(str(line).replace('\n', ''))
            print("Case #%s: %s" % (testcase_number, result))
            testcase_number = testcase_number + 1

ihop = Pancakes()