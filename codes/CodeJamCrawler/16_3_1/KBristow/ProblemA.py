def process_line(line1, line2):
    n_parties = int(line1)
    candidates_per_party_split=line2.strip().split()
    candidates_per_party = []
    total_candidates = 0
    for candidate_pop in candidates_per_party_split:
        candidates_per_party += [int(candidate_pop)]
        total_candidates += float(candidates_per_party[-1])

    evacuation_plan = build_evacuation_plan(candidates_per_party, total_candidates)
    evacuation_plan_string = ""
    for part in evacuation_plan:
        evacuation_plan_string += part + " "

    return evacuation_plan_string.strip()


def build_evacuation_plan(candidates_per_party, total_candidates):

    evacuation = []

    while total_candidates > 0:
        highest_indicies = find_highest_2(candidates_per_party)

        party_a = chr(65 + highest_indicies[0])
        party_b = chr(65 + highest_indicies[1])

        candidates_per_party[highest_indicies[0]] -= 2
        if test_solution(candidates_per_party, total_candidates - 2) and candidates_per_party[highest_indicies[0]] > 1:
            total_candidates -= 2
            evacuation += [party_a+party_a]
        else:
            candidates_per_party[highest_indicies[0]] += 1
            if test_solution(candidates_per_party, total_candidates - 1):
                total_candidates -= 1
                evacuation += [party_a]
            else:
                candidates_per_party[highest_indicies[1]] -= 1
                if test_solution(candidates_per_party, total_candidates - 2):
                    evacuation += [party_a + party_b]
                    total_candidates -= 2

    return evacuation


def test_solution(candidates_per_party, total_candidates):
    for population in candidates_per_party:
        if total_candidates == 0:
            break
        if population/total_candidates > 0.5:
            return False
    return True


def find_highest_2(candidates_per_party):
    highest = [0, 0]
    highest_indicies = [-1, -1]

    for i in range(0, len(candidates_per_party)):
        population = candidates_per_party[i]
        if population > highest[0]:
            highest[1] = highest[0]
            highest_indicies[1] = highest_indicies[1]
            highest[0] = population
            highest_indicies[0] = i
        elif population > highest[1]:
            highest[1] = population
            highest_indicies[1] = i

    return highest_indicies


year = 2016
problem_set = "LargeA"

with open(problem_set, 'r') as file_handle:
    lines = file_handle.readlines()


output_str = ""
for i in range(1, len(lines), 2):
    output_str += "Case #" + str((i+1)/2) + ": " + str(process_line(lines[i], lines[i+1])) + "\n"


output_str = output_str.strip()
print output_str
with open(str(year) + problem_set + ".out", "w") as file_handle:
    file_handle.write(output_str)


