from shared.codejam_plumbing import CodeJamInput, CodeJamOutput
import pickle, math, random

scenarios = CodeJamInput('input_files\A-large.in', 1)
outfile = CodeJamOutput('output_files\A-large-output', True)

scenarios = CodeJamInput('input_files\C-sample.in', 1)
outfile = CodeJamOutput('test_output.txt', True)

scenarioCount = scenarios.length


def learn_solutions(N, J):
    try:
        with open('output_files\c_pickle', 'rb') as f:
            coinjams = pickle.load(f)
    except:
        coinjams = dict()

    try:
        with open('output_files\c_pickle_factors.txt', 'rb') as f:
            known_factors = pickle.load(f)
    except:
        known_factors = dict()

    random_value = lambda length: '1' + str(bin(random.getrandbits(length-2)))[2:].zfill(length-2) + '1'
    print(random_value(N))

    while len(coinjams) < J:
        random_attempt = random_value(N)
        found = [True, True, False, False, False, False, False, False, False, False, False]
        solution = [0] * 9
        for base in range(2, 11):
            value = int(random_attempt, base)
            if value in known_factors:
                solution[base-2] = known_factors[value]
                found[base-2] = True
                print(value, "has factor %s in base %s" %(known_factors[value], base))
            else:
                ubound = math.ceil(math.sqrt(value))
                for potential_factor in range(4, ubound):
                    if potential_factor % 500000 == 1:
                        pass
                        print(random_attempt, "base", base, "==>", value, "??", potential_factor, "/", ubound)
                    if value % potential_factor == 0:
                        known_factors[value] = potential_factor
                        print("found factor:", str(potential_factor), 'for', value, "(base %s of %s)" %(base, random_attempt))
                        found[base] = True
                        solution[base-2] = potential_factor
                        break
                if value not in known_factors:
                    print('nothing found')
                    break

        if all(found):
            #then it is a coin jam!!!
            coinjams[random_attempt] = " ".join((str(x) for x in solution))
            with open('output_files\c_pickle', 'wb') as f:
                pickle.dump(coinjams, f)
            with open('output_files\c_pickle_factors.txt', 'wb') as f:
                pickle.dump(known_factors, f)
        else:
            "no go!"
        print('Found %s of %s coinjams' % (len(coinjams), J))
    print("Solutions:", len(coinjams))
    print(coinjams)

    with open('output_files\C-small-output', 'a') as f:
        f.write("Case #1:\n")
        f.write("\n".join(str(coin) + ' ' + str(coinjams[coin]) for coin in coinjams))

def solve():
    for case_number in range(1, scenarioCount+1):
        scenario_inputs = scenarios[case_number][0].strip('\n')


        def get_answer(inputs):
            N, J = inputs
            print(N, J)



        outfile[case_number] = get_answer(scenario_inputs.split(' '))

    outfile.save_results()

learn_solutions(16, 2)
