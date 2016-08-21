import string

abc = list(string.ascii_uppercase)

def find_max(l):
    max_element = max(l)
    max_list = [i for i, j in enumerate(l) if j == max_element]
    return max_list

def check_majority(l):
    n_senators = sum(l)
    for i in range(len(l)):
        if( l[i]/n_senators > 0.5 ):
            return False
    return True

def check_if_one(l):
    for i in range(len(l)):
        if (l[i] != 0) and (l[i] != 1):
            return False
    return True

def proces_list(l):
    output_string = ""
    while( sum(l) != 0):
        output_string = output_string + " "
        max_list = find_max(l)
        print(l)

        ones = check_if_one(l)
        if ones == True:
            if sum(l)%2 == 0:
                i_max_1 = max_list[0]
                i_max_2 = max_list[1]

                l[i_max_1] = l[i_max_1] - 1
                l[i_max_2] = l[i_max_2] - 1

                output_string = output_string + abc[i_max_1]
                output_string = output_string + abc[i_max_2]
                continue
            else:
                i_max = max_list[0]
                l[i_max] = l[i_max] - 1
                output_string = output_string + abc[i_max]
                continue

        if(len(max_list) >= 2):
            i_max_1 = max_list[0]
            i_max_2 = max_list[1]

            l[i_max_1] = l[i_max_1] - 1
            l[i_max_2] = l[i_max_2] - 1

            output_string = output_string + abc[i_max_1]
            output_string = output_string + abc[i_max_2]
            continue

        if(len(max_list) == 1):
            i_max = max_list[0]
            l[i_max] = l[i_max] - 1
            output_string = output_string + abc[i_max]
            continue

    return output_string

f = open("A-large.in", "r")
lines = f.readlines()

of = open("resL.txt","w")

j = 1
for i in range(2,len(lines),2):
    l = list(lines[i].split())
    l = [int(l[i]) for i in range(len(l))]
    c = "Case #" + str(j) +  ":"
    j = j + 1
    os = proces_list(l) + "\n"
    print(os)
    of.write(c + os)

of.close()





