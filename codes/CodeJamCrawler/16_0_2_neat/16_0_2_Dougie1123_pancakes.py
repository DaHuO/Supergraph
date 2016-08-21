f = open('input.txt')
lines = f.readlines()
f.close()

def min_flips_neg(pan):
    #base case
    if pan == "-":
        return 0
    elif pan == '+':
        return 1
    else:
        print(pan)
        back_idx = -1
        back = pan[back_idx]
        for i in range(len(pan) - 1):
            # not same elem
            if pan[back_idx] != back:
                break
            back_idx -= 1
        if back == '-':
            return min_flips_neg(pan[0:len(pan) + back_idx + 1])
        else:
            return 1 + min_flips_pos(pan[0:len(pan) + back_idx + 1])


def min_flips_pos(pan):
    #base case
    if pan == "-":
        return 1
    elif pan == '+':
        return 0
    else:
        print(pan)
        back_idx = -1
        back = pan[back_idx]
        for i in range(len(pan)-1):
            #not same elem
            if pan[back_idx] != back:
                break
            back_idx -= 1

        if back == '-':
            return 1 + min_flips_neg(pan[0:len(pan)+back_idx+1])
        else:
            return min_flips_pos(pan[0:len(pan)+back_idx+1])


output = open('output.txt','w')
for i in range(int(lines[0])):
    pan = lines[i+1].strip()
    num_flips = min_flips_pos(pan)


    output.write("Case #" + str(i+1) + ": " + str(num_flips) + "\n")
output.close()