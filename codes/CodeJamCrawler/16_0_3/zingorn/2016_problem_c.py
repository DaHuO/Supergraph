dir = "./"
in_name = dir + "input_1.txt"

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
    while array_of_primes[i] <= sqr:
        if (candidate_number % array_of_primes[i] == 0):
            return array_of_primes[i]
        i += 1
        if i > max_index_from_file:
            return "XXX!"                              # to small file of primals  # skip "SURPRISE!" with hope on next numbers
    return 1                                                # is primal

f_in = open(in_name)
out_name = "output_1.txt"
f_out = open(out_name, 'w')

file_primes = dir + "Primes_6"         # external file with many primals
txt_primes = open(file_primes)
array_of_primes = []
for line in txt_primes:
    array_of_primes.append(int(line))
max_index_from_file = len(array_of_primes)-1
max_primal_from_file = array_of_primes[max_index_from_file]        # largest primal from file

number_of_tests = int(f_in.readline())

test_number = 1

while test_number <= number_of_tests:
    v_line = f_in.readline()
    info = v_line.split()
    v_N = int(info[0])
    v_J = int(info[1])

    v_N_min = pow(10, v_N-1) + 1
    v_N_max = int(str(bin(pow(2, v_N) - 1))[2:])     # [2:] = delete '0b' from binary view
    print(v_N_min)
    print(v_N_max)
    v_sqr = int(pow(v_N_max, 0.5) // 1)                 # // 1 = integer part of the division
    print(v_sqr)

    f_out.write("Case #" + str(test_number) + ":" + "\n")
    answer_number = 0
    i = 0
    while i <= pow(2, v_N-2)-1:      # it's a middle - N-2 digits - (because first and last digits are always '1')
        candidate = '1' + str(bin(i))[2:].zfill(v_N-2) + '1'   # [2:] = delete '0b' from binary view

        base = 2
        is_answer = 1
        answer = str(number_by_base(candidate, 10))
        while base <= 10:
            number = number_by_base(candidate, base)
            print(str(base) + ' - ' + str(number))
            _is_primal = is_primal(number)
            if _is_primal != 1 and _is_primal != "XXX!":     # skip "SURPRISE!" with hope on next numbers
                answer += " " + str(_is_primal)
            else:
                is_answer = 0
                break

            base += 1

        if is_answer == 1:
            f_out.write(answer + "\n")
            answer_number += 1

        if answer_number == v_J:
            break

        i += 1

    test_number += 1

