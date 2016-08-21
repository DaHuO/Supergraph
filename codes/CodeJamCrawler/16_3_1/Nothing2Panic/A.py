
import sys

parties = ["A",'B','C','D','E','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']


def process_Ns_line(Ns_str):
    Ns_strS = Ns_str.split()
    Ns = []
    for val in Ns_strS:
        Ns.append(int(val))
    return Ns
        

def findMosTwo(Ns):
    most1_val= 0
    most2_val = 0
    most1_p = 0 
    most2_p = 0

    for index in range(0,len(Ns)):
        if Ns[index] > most1_val:
            most1_val = Ns[index]
            most1_p = index
        elif Ns[index] > most2_val:
            most2_val = Ns[index]
            most2_p = index

    if most2_val == 0:
        most2_val = Ns[-2]
        most2_p = len(Ns) - 2

    if most1_val >= most2_val+2:
        return (most1_p,most1_p)
    else:
        return (most1_p,most2_p)

def convert_Ps_to_Cs(mostPs):
    step = ""
    step = convert_P_to_C(mostPs[0] ) + convert_P_to_C(mostPs[1])
    return step

def convert_P_to_C(P):
    return parties[P]

def process_case(N, Ns):
    ans = ""
    steps = sum(Ns) /2

    #for step in range(0,steps):
    
    for step in range(0, steps-1):
        mostPs = findMosTwo(Ns)
        Ns[mostPs[0]] = Ns[mostPs[0]] -1
        Ns[mostPs[1]] = Ns[mostPs[1]]-1
        step_ans = convert_Ps_to_Cs(mostPs)
        ans = ans + step_ans + " "

    last_steps = sum(Ns)
    if last_steps == 2:
        mostPs = findMosTwo(Ns)
        step_ans = convert_Ps_to_Cs(mostPs)
        ans = ans + step_ans + " "

    elif last_steps == 3:
        mostPs = findMosTwo(Ns)
        Ns[mostPs[0]] = Ns[mostPs[0]] - 1
        step_ans = convert_P_to_C(mostPs[0])
        ans = ans + step_ans + " "
        
        mostPs = findMosTwo(Ns)
        step_ans =convert_Ps_to_Cs(mostPs)
        ans = ans + step_ans + " "

    return ans

    



if __name__ == "__main__":
    file_name = sys.argv[1]
    file_case = open(file_name,"r")
    T_str = file_case.readline()
    T = int(T_str)
    print T

    for idx in range(0,T):
        N_str = file_case.readline()
        N = int(N_str)
        print N
        Ns_str = file_case.readline()
        Ns = process_Ns_line(Ns_str)
        print Ns
        ans = process_case(N,Ns)
        ans = "Case #" + str(idx+1) + ": " + ans
        print ans
        with open('output','a') as outputFile:
            outputFile.write(ans+"\n")
        

    
