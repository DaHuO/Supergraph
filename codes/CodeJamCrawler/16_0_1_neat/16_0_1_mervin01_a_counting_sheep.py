from shared.codejam_plumbing import CodeJamInput, CodeJamOutput

scenarios = CodeJamInput('input_files\A-large.in', 1)
outfile = CodeJamOutput('output_files\A-large-output', True)

scenarioCount = scenarios.length

for case_number in range(1, scenarioCount+1):
    scenario_inputs = scenarios[case_number][0].strip('\n')
    print(case_number, scenario_inputs)

    def get_answer(starting_number):
        numbers_seen = [False, False, False, False, False, False, False, False, False, False]

        for n in range(1, 100):
            x = int(starting_number)
            nx = n * x
            #print('.', nx,)
            for digit in str(nx):
                numbers_seen[int(digit)] = True
                #print(numbers_seen)
            if all(numbers_seen):
                return nx
        return None

    outfile[case_number] = get_answer(int(scenario_inputs))
outfile.save_results()
