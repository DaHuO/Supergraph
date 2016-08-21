from shared.codejam_plumbing import CodeJamInput, CodeJamOutput
_CodeJamRound = "2016.1A"
_Question = "A"
_AttemptNo = 0

_RowsPerInput = 1

large_files = ('inputs\%s-large.in' % _Question, 'outputs\%s-large-output' % _Question)
small_files = ('inputs\%s-small-attempt%s.in' % (_Question, _AttemptNo), 'outputs\%s-small-output' % _Question)
sample_files = (r'inputs\%s-sample.in' % _Question, r'outputs\test_output.txt')
f_in, f_out = large_files

scenarios = CodeJamInput(f_in, _RowsPerInput)
outfile = CodeJamOutput(f_out, debug=True)
scenarioCount = scenarios.length
outfile.NoneSolution = "IMPOSSIBLE"     # TODO: Update this

for case_number in range(1, scenarioCount+1):
    scenario_inputs = scenarios[case_number][0].strip('\n')
    print(case_number)

    def solve_case(inputs):
        print(inputs)
        temp_string = inputs[0]
        for letter in inputs[1:]:
            if ord(letter) >= ord(temp_string[0]):
                temp_string = letter + temp_string
            else:
                temp_string = temp_string + letter

        return temp_string


    outfile[case_number] = solve_case(scenario_inputs)
outfile.save_results()
