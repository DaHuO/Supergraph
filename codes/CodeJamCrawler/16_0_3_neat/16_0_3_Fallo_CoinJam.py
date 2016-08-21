import math
from sympy.ntheory import factorint
import sympy
__author__ = 'FalguniT'

# define a function
def find_factors(x):
    factors = []
    if not(sympy.isprime(x)):
        dict_factors = factorint(x)
        for base, exp in sorted(dict_factors.items()):
            factors.append(base)
    return factors


def main():
    with open("input_coinjam.txt") as f:
        content = f.readlines()
    no_of_test_cases = int(content[0])

    for case_t in range(1,no_of_test_cases + 1):
        with open("output_coinjam.txt","a") as f_handle:
                f_handle.write('Case #'+ str(case_t) + ':\n')
        input_value = content[case_t].strip()

        n = int(input_value.split()[0])
        j = int(input_value.split()[1])

        coin_jam_sol = []
        coin_jan_sol_count = 0
        #possible_combination = int(math.pow(2, n-2))
        #print(possible_combination)
        possible_codejamvalues = [bin(x)[2:].rjust(n, '0') for x in range(2**n)]

        #select with starting and trailing ones
        possible_codejamvalues = [x for x in possible_codejamvalues if (x[0] == '1' and x[n-1] == '1')]
        print(possible_codejamvalues)

        #print("possible_codejamvalues", possible_codejamvalues)

        for coin_jam in range(1, len(possible_codejamvalues)):
            base_2_value = int(possible_codejamvalues[coin_jam], 2)
            base_3_value = int(possible_codejamvalues[coin_jam], 3)
            base_4_value = int(possible_codejamvalues[coin_jam], 4)
            base_5_value = int(possible_codejamvalues[coin_jam], 5)
            base_6_value = int(possible_codejamvalues[coin_jam], 6)
            base_7_value = int(possible_codejamvalues[coin_jam], 7)
            base_8_value = int(possible_codejamvalues[coin_jam], 8)
            base_9_value = int(possible_codejamvalues[coin_jam], 9)
            base_10_value = int(possible_codejamvalues[coin_jam], 10)

            print("coin_jam", possible_codejamvalues[coin_jam])
            base_2_factors = find_factors(base_2_value)
            if len(base_2_factors) == 0:
                continue
            base_3_factors = find_factors(base_3_value)
            if len(base_3_factors) == 0:
                continue
            base_4_factors = find_factors(base_4_value)
            if len(base_4_factors) == 0:
                continue
            base_5_factors = find_factors(base_5_value)
            if len(base_5_factors) == 0:
                continue
            base_6_factors = find_factors(base_6_value)
            if len(base_6_factors) == 0:
                continue
            base_7_factors = find_factors(base_7_value)
            if len(base_7_factors) == 0:
                continue
            base_8_factors = find_factors(base_8_value)
            if len(base_8_factors) == 0:
                continue
            base_9_factors = find_factors(base_9_value)
            if len(base_9_factors) == 0:
                continue
            base_10_factors = find_factors(base_10_value)
            if len(base_10_factors) == 0:
                continue

            #print("coin_jam", possible_codejamvalues[coin_jam])
            print(base_2_value, base_2_factors)
            print(base_3_value, base_3_factors)
            print(base_4_value, base_4_factors)
            print(base_5_value, base_5_factors)
            print(base_6_value, base_6_factors)
            print(base_7_value, base_7_factors)
            print(base_8_value, base_8_factors)
            print(base_9_value, base_9_factors)
            print(base_10_value, base_10_factors)

            codejam_sol = []
            codejam_sol.append(base_2_factors[0])
            codejam_sol.append([t for t in base_3_factors if t not in codejam_sol][0])
            codejam_sol.append([t for t in base_4_factors if t not in codejam_sol][0])
            codejam_sol.append([t for t in base_5_factors if t not in codejam_sol][0])
            codejam_sol.append([t for t in base_6_factors if t not in codejam_sol][0])
            codejam_sol.append([t for t in base_7_factors if t not in codejam_sol][0])
            codejam_sol.append([t for t in base_8_factors if t not in codejam_sol][0])
            codejam_sol.append([t for t in base_9_factors if t not in codejam_sol][0])
            codejam_sol.append([t for t in base_10_factors if t not in codejam_sol][0])

            if (len(codejam_sol) == 9):
                coin_jam_sol.append(codejam_sol)
                print("coin_jam_sol", codejam_sol)
                with open("output_coinjam.txt","a") as f_handle:
                    f_handle.write(possible_codejamvalues[coin_jam] + '\t\t' + str(codejam_sol).replace('L','').replace(',','\t').replace('[','').replace(']','') + '\n')
                    f_handle.close()

                coin_jan_sol_count = coin_jan_sol_count+ 1


            if(coin_jan_sol_count == j):
                break



main()