from shared.codejam_plumbing import GCJParsedInput, GCJOutputs
import re

_CodeJamRound = "2016.1B"
_Question = "A"
_AttemptNo = 1
_SmallLargeSample = 'large'        # pick between 'sample', 'small' (requires attemptNo), 'large', 'practice'

assert _SmallLargeSample in ('sample', 'small', 'large', 'practice'), "Invalid configuration"

files = {'large': ('inputs\%s-large.in' % _Question, 'outputs\%s-large-output' % _Question),
         'small': ('inputs\%s-small-attempt%s.in' % (_Question, _AttemptNo), 'outputs\%s-small-output' % _Question),
         'sample': (r'inputs\%s-sample.in' % _Question, r'outputs\test_output.txt'),
         'practice': (r'inputs\%s-small-practice.in' % _Question, r'outputs\%s-small-practice-output.txt' % _Question)}
f_in, f_out = files[_SmallLargeSample]

scenarios = GCJParsedInput(file_path=f_in, len_type="fixed", len_function=1)
outfile = GCJOutputs(file_path=f_out, failure_response='xx')

for caseNo, caseData in scenarios:
    print(caseNo, caseData)

    def solve_case(inputs):

        solution = None
        garbled = str(inputs[0].strip('\n'))
        mangled = ''.join(sorted(garbled))
        print(mangled)
        unparsed = dict()
        parsed = ''
        for letter in mangled.lower():
            if letter in unparsed:
                unparsed[letter] += 1
            else:
                unparsed[letter] = 1
        print(unparsed)

        rules = (
                ('z', 'zero', '0'), ('w', 'two', '2'), ('x', 'six', '6'), ('g', 'eight', '8'),
                ('h', 'three', '3'), ('r', 'four', '4'), ('f', 'five', '5'), ('v', 'seven', '7'),
                ('o', 'one', '1'), ('i', 'nine', '9')
                 )

        for character, word, digit in rules:
            if character in unparsed:
                if unparsed[character] > 0:
                    count = unparsed[character]
                    # print("found %s times %s's" % (count, digit))
                    parsed += digit*count
                    for x in word:
                        unparsed[x] -= count
        sums = sum(x for x in unparsed.values())
        assert sums == 0
        if sums != 0:
            print(unparsed, garbled)

        return "".join(sorted(parsed))




    outfile[caseNo+1] = solve_case(caseData)
outfile.save_results()


""" Contents of codejam.plumbing (pasted for completeness)"""
# class GCJOutputs:
#     def __init__(self, file_path, failure_response=None, debug=False):
#         self.file = file_path
#         self.answers = dict()
#         self.debugOn = debug
#         self.answerPrefix = "Case #%s: "
#         self.NoneSolution = failure_response
#
#     def save_results(self):
#         answers = list()
#         for case in range(1, len(self.answers) + 1):
#             caseNo, caseSolution = self.answers[case]
#             if caseSolution is None:
#                 caseSolution = self.NoneSolution
#             sOutput = self.answerPrefix + str(caseSolution)
#             answers.append(sOutput % caseNo)
#
#         with open(self.file, "a") as f:
#             f.write('\n'.join(answers))
#
#     def __setitem__(self, key, value):
#         if value is None:
#             if self.NoneSolution == 'raise':
#                 raise ValueError('case cannot have a solution of None')
#             else:
#                 value = self.NoneSolution
#         self.answers[key] = (key, value)
#         if self.debugOn:
#             print(self.answerPrefix % key, value)
#
# class GCJParsedInput:
#     def __init__(self, file_path, len_type="fixed", len_function=1):
#         with open(file_path) as inp:
#             self.raw = inp.readlines()
#         self.length = int(self.raw[0])
#         self.scenarios = dict()
#
#         cursor_at_line = 1
#         while len(self.scenarios) < self.length:
#             if len_type == "fixed":
#                 self.scenarios[len(self.scenarios)] = self.raw[cursor_at_line:cursor_at_line + len_function]
#                 cursor_at_line += len_function
#             elif len_type == "function":
#                 x = int(self.raw[cursor_at_line].strip("\n"))
#                 self.scenarios[len(self.scenarios)] = self.raw[cursor_at_line:cursor_at_line + len_function(x)]
#                 cursor_at_line += len_function(x)
#             else:
#                 raise ValueError
#         print("Parsed", self.scenarios)
#
#     def __len__(self):
#         return self.length
#
#     def __getitem__(self, item):
#         return self.scenarios[item]
#
#     def __iter__(self):
#         for x in self.scenarios:
#             yield x, self.scenarios[x]

