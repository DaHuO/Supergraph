from shared.codejam_plumbing import CodeJamInput, CodeJamOutput

question = 'B'
attemptNo = 0
large_files = ('input_files\%s-large.in' % question, 'output_files\%s-large-output' % question)
small_files = ('input_files\%s-small-attempt%s.in' %(question, attemptNo), 'output_files\%s-small-output' % question)
sample_files = ('input_files\%s-sample.in' % question, 'test_output.txt')

files = large_files

scenarios = CodeJamInput(files[0], 1)
outfile = CodeJamOutput(files[1], True)

scenarioCount = scenarios.length

for case_number in range(1, scenarioCount+1):
    scenario_inputs = scenarios[case_number][0].strip('\n')


    def get_answer(starting_stack):
        print(starting_stack)
        adjusted_stack = starting_stack + '+'
        count_zones = 1
        for pos in range(1, len(adjusted_stack)):
            a,b = adjusted_stack[pos-1:pos+1]
            if a != b:
                count_zones += 1
        return count_zones-1


    outfile[case_number] = get_answer(str(scenario_inputs))
outfile.save_results()
