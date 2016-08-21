v_dir = "k:\\Python\\codejam\\2016_problem_c\\"
v_file_input = v_dir + "input_1.txt"
# filename = v_dir + "A-small-practice.in"
# filename = v_dir + "A-large-practice.in"

def number_by_base(candidate, base):
    i = 0
    result = 0
    while i <= v_N-1:
        result += int(candidate[i]) * pow(base, v_N-1-i)
        i += 1
    return result

def is_primal(candidate_number):                            # return Divider or '1' for primal
    i = 0
    sqr = int(pow(candidate_number, 0.5) // 1)
    while v_array_of_primes[i] <= sqr:
        if (candidate_number % v_array_of_primes[i] == 0):
            return v_array_of_primes[i]
        i += 1
        if i > v_max_index_from_file:
            return "SURPRISE!"                              # to small file of primals  # skip "SURPRISE!" with hope on next numbers
    return 1                                                # is primal

v_txt_in = open(v_file_input)
v_file_output = "output_1.txt"
v_txt_out = open(v_file_output, 'w')

v_file_primes = v_dir + "Primes_16"         # external file with many primals
v_txt_primes = open(v_file_primes)
v_array_of_primes = []
for line in v_txt_primes:
    v_array_of_primes.append(int(line))
v_max_index_from_file = len(v_array_of_primes)-1
v_max_primal_from_file = v_array_of_primes[v_max_index_from_file]        # largest primal from file
# print(v_max_primal_from_file)

v_number_of_tests = int(v_txt_in.readline())

v_test_number = 1

while v_test_number <= v_number_of_tests:
    v_line = v_txt_in.readline()
    info = v_line.split()
    v_N = int(info[0])
    v_J = int(info[1])

    v_N_min = pow(10, v_N-1) + 1
    v_N_max = int(str(bin(pow(2, v_N) - 1))[2:])     # [2:] = delete '0b' from binary view
    print(v_N_min)
    print(v_N_max)
    v_sqr = int(pow(v_N_max, 0.5) // 1)                 # // 1 = integer part of the division
    print(v_sqr)
    #v_N_middle = int(str(bin(pow(2, v_N-2) - 1))[2:])   # string with N-2 of '1' (because first and last digits are always '1')
    #print(v_N_middle)

    v_txt_out.write("Case #" + str(v_test_number) + ":" + "\n")
    v_answer_number = 0
    i = 0
    while i <= pow(2, v_N-2)-1:      # it's a middle - N-2 digits - (because first and last digits are always '1')
        v_candidate = '1' + str(bin(i))[2:].zfill(v_N-2) + '1'   # [2:] = delete '0b' from binary view
        print('========')
        print(v_candidate)

        v_base = 2
        v_is_answer = 1
        v_answer = str(number_by_base(v_candidate, 10))
        while v_base <= 10:
            v_number = number_by_base(v_candidate, v_base)
            print(str(v_base) + ' - ' + str(v_number))
            v_is_primal = is_primal(v_number)
            if v_is_primal != 1 and v_is_primal != "SURPRISE!":     # skip "SURPRISE!" with hope on next numbers
                v_answer += " " + str(v_is_primal)
            else:
                v_is_answer = 0
                break

            v_base += 1

        if v_is_answer == 1:
            v_txt_out.write(v_answer + "\n")
            v_answer_number += 1

        if v_answer_number == v_J:
            break

        i += 1

    #print(answer)
    v_test_number += 1

