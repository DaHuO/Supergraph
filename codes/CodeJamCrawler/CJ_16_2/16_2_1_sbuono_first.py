import sys

__author__ = 'PC'


def output(out, tc, res):
    print("Case #%s: %s" % (tc, res))
    out.write("Case #%s: %s\n" % (tc, res))

with open('output', 'w+') as out:
    with open(sys.argv[1], 'r') as f:
        T = int(f.readline())
        for tc in range(1, T + 1):
            S = f.readline()

            dct = dict()
            numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for letter in S:
                if letter not in dct.keys():
                    dct[letter] = 0
                dct[letter] += 1

            print S
            print dct
            if "Z" in dct.keys() and dct["Z"] != 0:
                nb_z = dct["Z"]
                dct["Z"] = 0
                dct["E"] -= nb_z
                dct["R"] -= nb_z
                dct["O"] -= nb_z
                numbers[0] = nb_z

            if "W" in dct.keys() and dct["W"] != 0:
                nb_w = dct["W"]
                dct["T"] -= nb_w
                dct["W"] = 0
                dct["O"] -= nb_w
                numbers[2] = nb_w

            if "U" in dct.keys() and dct["U"] != 0:
                nb_u = dct["U"]
                dct["F"] -= nb_u
                dct["O"] -= nb_u
                dct["U"] = 0
                dct["R"] -= nb_u
                numbers[4] = nb_u

            if "X" in dct.keys() and dct["X"] != 0:
                nb_x = dct["X"]
                dct["S"] -= nb_x
                dct["I"] -= nb_x
                dct["X"] = 0
                numbers[6] = nb_x

            if "G" in dct.keys() and dct["G"] != 0:
                nb_g = dct["G"]
                dct["E"] -= nb_g
                dct["I"] -= nb_g
                dct["G"] = 0
                dct["H"] -= nb_g
                dct["T"] -= nb_g
                numbers[8] = nb_g

            if "T" in dct.keys() and dct["T"] != 0:
                nb_t = dct["T"]
                dct["T"] = 0
                dct["H"] -= nb_t
                dct["R"] -= nb_t
                dct["E"] -= nb_t
                dct["E"] -= nb_t
                numbers[3] = nb_t

            if "S" in dct.keys() and dct["S"] != 0:
                nb_s = dct["S"]
                dct["S"] = 0
                dct["E"] -= nb_s
                dct["V"] -= nb_s
                dct["E"] -= nb_s
                dct["N"] -= nb_s
                numbers[7] = nb_s

            if "V" in dct.keys() and dct["V"] != 0:
                nb_v = dct["V"]
                dct["F"] -= nb_v
                dct["I"] -= nb_v
                dct["V"] = 0
                dct["E"] -= nb_v
                numbers[5] = nb_v

            if "I" in dct.keys() and dct["I"] != 0:
                nb_i = dct["I"]
                dct["N"] -= nb_i
                dct["I"] = 0
                dct["N"] -= nb_i
                dct["E"] -= nb_i
                numbers[9] = nb_i

            if "O" in dct.keys() and dct["O"] != 0:
                nb_o = dct["O"]
                # dct["N"] -= nb_i
                # dct["I"] = 0
                # dct["N"] -= nb_i
                # dct["E"] -= nb_i
                numbers[1] = nb_o

            nbs = []
            for i in range(len(numbers)):
                nbs.append(str(i) * numbers[i])
            output(out, tc, "".join(nbs))