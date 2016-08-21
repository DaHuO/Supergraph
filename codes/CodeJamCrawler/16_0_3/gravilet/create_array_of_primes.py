v_dir = "k:\\Python\\codejam\\2016_problem_c\\"
#v_file_input = v_dir + "input_1.txt"
# filename = v_dir + "A-small-practice.in"
# filename = v_dir + "A-large-practice.in"

###
### CREATE LIST of ALL PRIMES from 2 to sqrt(111..111)
###

v_N = 18     # v_N digits - 111..111
v_file_output_Primes = "Primes_" + str(v_N)
v_txt_out = open(v_file_output_Primes, 'w')


v_N_max = int(str(bin(pow(2, v_N) - 1))[2:])     # [2:] = delete '0b' from binary view
print(v_N_max)
v_N_sqr = int(pow(v_N_max, 0.5) // 1)                 # // 1 = integer part of the division
print(v_N_sqr)

i = 11
v_array_of_primes = [2,3,5,7]       # first primes
for y in v_array_of_primes:
    v_txt_out.write(str(y) + "\n")

while i <= v_N_sqr:
    v_sqr = int(pow(i, 0.5) // 1)
    for y in v_array_of_primes:
        if ((i % y) == 0):
            break
        if y > v_sqr:
            v_array_of_primes.append(i)
            v_txt_out.write(str(i) + "\n")
            break
    i += 2
    print(i)



