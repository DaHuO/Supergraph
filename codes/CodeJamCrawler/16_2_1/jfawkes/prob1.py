import sys
import math
from copy import deepcopy


    
def print_ans(case_num,solution):
    print("Case #"+str(case_num)+":"),
    print_solution(solution)

def print_solution(solution):
    """TO DO"""
    print solution


def input_processor(filename):
    f=open(filename)
    data=f.read().split("\n")
    case_nums=int(data[0])

    """Insert number of lines per test case here"""
    num_of_lines=1
    data_length=len(data)

    """Edit start_index here"""
    start_index=1
    case_num=1
    

    for i in xrange(0,case_nums):
        start=(i*num_of_lines)+start_index
        problem=data[start:start+num_of_lines]
        process_input_case(case_num,problem)
        case_num+=1

def process_input_case(case_num,problem):
    """Process raw input into apropriate type"""
    problem_variable = problem[0]
    solve(case_num,problem_variable)

def solve(case_num,problem_variable):
    index_list ={}
    for c in problem_variable:
        if c not in index_list:
            index_list[c] = 0
        index_list[c]+=1

    result, amari = recurse(index_list)
    result = sorted(result)
    solution = ""
    for c in result:
        solution+= str(c)


    print_ans(case_num, solution)

def recurse(index_list):
    #print index_list
    dict_copy = deepcopy(index_list)
    if "O" in dict_copy and dict_copy["O"] >=1:
        if "N" in dict_copy and dict_copy["N"] >=1:

            if "E" in dict_copy and dict_copy["E"] >=1:
                dict_copy["O"]-=1
                dict_copy["N"]-=1
                dict_copy["E"]-=1
                result, amari = recurse(dict_copy)
                count = 0
                for key,value in amari.iteritems():
                    count+=value
                    if value != 0:
                        break
                if count == 0:
                    return [1]+result , amari

    dict_copy = deepcopy(index_list)

    if "T" in dict_copy and dict_copy["T"] >=1:
        if "W" in dict_copy and dict_copy["W"] >=1:
            if "O" in dict_copy and dict_copy["O"] >=1:
                dict_copy["T"]-=1
                dict_copy["W"]-=1
                dict_copy["O"]-=1
                result, amari = recurse(dict_copy)
                count = 0
                for key,value in amari.iteritems():
                    count+=value
                    if value != 0:
                        break
                if count == 0:
                    return [2]+result , amari
    dict_copy = deepcopy(index_list)

    if "T" in dict_copy and dict_copy["T"] >=1:
        if "H" in dict_copy and dict_copy["H"] >=1:
            if "R" in dict_copy and dict_copy["R"] >=1:
                if "E" in dict_copy and dict_copy["E"] >=2:
                    dict_copy["T"]-=1
                    dict_copy["H"]-=1
                    dict_copy["R"]-=1
                    dict_copy["E"]-=2
                    result, amari = recurse(dict_copy)
                    count = 0
                    for key,value in amari.iteritems():
                        count+=value
                        if value != 0:
                            break
                    if count == 0:
                        return [3]+result , amari
    dict_copy = deepcopy(index_list)

    if "F" in dict_copy and dict_copy["F"] >=1:
        if "O" in dict_copy and dict_copy["O"] >=1:
            if "U" in dict_copy and dict_copy["U"] >=1:
                if "R" in dict_copy and dict_copy["R"] >=1:
                    dict_copy["F"]-=1
                    dict_copy["O"]-=1
                    dict_copy["U"]-=1
                    dict_copy["R"]-=1
                    result, amari = recurse(dict_copy)
                    count = 0
                    for key,value in amari.iteritems():
                        count+=value
                        if value != 0:
                            break
                    if count == 0:
                        return [4]+result , amari

    dict_copy = deepcopy(index_list)

    if "F" in dict_copy and dict_copy["F"] >=1:
        if "I" in dict_copy and dict_copy["I"] >=1:
            if "V" in dict_copy and dict_copy["V"] >=1:
                if "E" in dict_copy and dict_copy["E"] >=1:
                    dict_copy["F"]-=1
                    dict_copy["I"]-=1
                    dict_copy["V"]-=1
                    dict_copy["E"]-=1
                    result, amari = recurse(dict_copy)
                    count = 0
                    for key,value in amari.iteritems():
                        count+=value
                        if value != 0:
                            break
                    if count == 0:
                        return [5]+result , amari
    dict_copy = deepcopy(index_list)

    if "S" in dict_copy and dict_copy["S"] >=1:
        if "I" in dict_copy and dict_copy["I"] >=1:
            if "X" in dict_copy and dict_copy["X"] >=1:
                dict_copy["S"]-=1
                dict_copy["I"]-=1
                dict_copy["X"]-=1
                result, amari = recurse(dict_copy)
                count = 0
                for key,value in amari.iteritems():
                    count+=value
                    if value != 0:
                        break
                if count == 0:
                    return [6]+result , amari
    dict_copy = deepcopy(index_list)

    if "S" in dict_copy and dict_copy["S"] >=1:
        if "E" in dict_copy and dict_copy["E"] >=2:
            if "V" in dict_copy and dict_copy["V"] >=1:
                if "N" in dict_copy and dict_copy["N"] >=1:
                    dict_copy["S"]-=1
                    dict_copy["E"]-=2
                    dict_copy["V"]-=1
                    dict_copy["N"]-=1
                    result, amari = recurse(dict_copy)
                    count = 0
                    for key,value in amari.iteritems():
                        count+=value
                        if value != 0:
                            break
                    if count == 0:
                        return [7]+result , amari
    dict_copy = deepcopy(index_list)

    if "E" in dict_copy and dict_copy["E"] >=1:
        if "I" in dict_copy and dict_copy["I"] >=1:
            if "G" in dict_copy and dict_copy["G"] >=1:
                if "H" in dict_copy and dict_copy["H"] >=1:
                    if "T" in dict_copy and dict_copy["T"] >=1:
                        dict_copy["E"]-=1
                        dict_copy["I"]-=1
                        dict_copy["G"]-=1
                        dict_copy["H"]-=1
                        dict_copy["T"]-=1

                        result, amari = recurse(dict_copy)
                        count = 0
                        for key,value in amari.iteritems():
                            count+=value
                            if value != 0:
                                break
                        if count == 0:
                            return [8]+result , amari

    dict_copy = deepcopy(index_list)

    if "N" in dict_copy and dict_copy["N"] >=2:
        if "I" in dict_copy and dict_copy["I"] >=1:
            if "E" in dict_copy and dict_copy["E"] >=1:
                dict_copy["N"]-=2
                dict_copy["I"]-=1
                dict_copy["E"]-=1
                result, amari = recurse(dict_copy)
                count = 0
                for key,value in amari.iteritems():
                    count+=value
                    if value != 0:
                        break
                if count == 0:
                    return [9]+result , amari

    dict_copy = deepcopy(index_list)

    if "Z" in dict_copy and dict_copy["Z"] >=1:
        if "E" in dict_copy and dict_copy["E"] >=1:
            if "R" in dict_copy and dict_copy["R"] >=1:
                if "O" in dict_copy and dict_copy["O"] >=1:
                    dict_copy["Z"]-=1
                    dict_copy["E"]-=1
                    dict_copy["R"]-=1
                    dict_copy["O"]-=1
                    result, amari = recurse(dict_copy)
                    count = 0
                    for key,value in amari.iteritems():
                        count+=value
                        if value != 0:
                            break
                    if count == 0:
                        return [0]+result , amari

    return [], index_list










def main():
    input_file=sys.argv[1]
    input_processor(input_file)


if __name__=="__main__":
    main()