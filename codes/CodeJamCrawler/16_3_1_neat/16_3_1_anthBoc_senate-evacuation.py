alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',\
 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

senators = ['2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',\
 '0', '0', '0', '0', '0', '0', '0']

s = [3, 2, 2]

#Check if there is a majority
def majority(senators):
    for s in senators:
        if s > sum(senators) - s:
            return True
    return False




def remove_one_max(senators):
    s = copy(senators)
    index_max = s.index(max(s))
    s[index_max] -= 1
    return s

def remove_two_max(senators):
    s = copy(senators)
    index_max = s.index(max(s))

    s2 = s[0:index_max] + [s[index_max] -2] + (s[index_max+1:] if index_max < len(s) else [])
    if s[index_max] >= 2 and not majority(s2):
        return s2
    else:
        s = remove_one_max(s)
        s = remove_one_max(s)
    return s



def get_index_one_max(senators):
    return senators.index(max(senators))

def get_index_two_max(senators):
    index_max = senators.index(max(senators))
    s2 = senators[0:index_max] + [senators[index_max] -2] + (senators[index_max+1:] if index_max < len(senators) else [])
    if senators[index_max] >= 2 and not majority(s2):
        return [index_max, index_max]
    else:
        ret = [get_index_one_max(senators)]
        s = remove_one_max(senators)
        ret += [get_index_one_max(s)]
        s = remove_one_max(senators)
        return ret


def copy(s):
    return s[:]




def evacuate(senators):
    ret = ""
    while max(senators) > 0:
        if (not majority(remove_one_max(senators))):
            ret += " " + chr(get_index_one_max(senators) + 65)
            senators = remove_one_max(senators)
        elif (not majority(remove_two_max(senators))):
            indexes_max = get_index_two_max(senators)
            ret += " "
            for index in indexes_max:
                ret += chr(index + 65)
            senators = remove_two_max(senators)
        else:
            print("ERROR: ")
            print(senators)
    return ret[1:]





def main():
    result = ""
    i = 1

    #Open the input file
    with open("A-large.in", 'r') as inputFile:
        testCasesNumber = inputFile.readline()
        #Every case
        while i <= int(testCasesNumber):
            matrix = []
            N = int(inputFile.readline())
            line = inputFile.readline()
            line = line.replace('\n', "")
            matrix = line.split(' ')
            matrix = map(int, matrix)
            result += "Case #" + str(i) + ": "  + evacuate(matrix) + '\n'
            i += 1
    #Write result
    with open("output.txt", 'w') as outputFile:
        outputFile.write(result)


#print(evacuate(s))
main()
