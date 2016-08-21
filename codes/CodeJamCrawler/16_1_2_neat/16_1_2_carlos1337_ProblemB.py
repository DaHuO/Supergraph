
def check_if_valid(total_array, paper):
    valid = True
    for index,elem in enumerate(total_array):
        if(elem >= paper[index % N]):
            valid = False
            break
    return valid

def check_if_fits(total_array, column):        
    for index in range(N):
        valid = True
        ##print("Skipping "+str(skip))
        dummyIndex = 0        
        for index2 in range(N):     
            ##print("Checking"+str(column[index2])+"<>"+str(total_array[dummyIndex*N+index]))
            if(column[index2]!=total_array[dummyIndex*N+index]):
                valid=False
            dummyIndex+=1
        if(valid):
            return True                
    return False

def combine(total_array,number,my_list, used):
    if number==0:
        not_used = [index for index,e in enumerate(used) if not e]
        for index in not_used:
            ##print(str(my_list[index]) + " fits in "+str(total_array)+"?")
            current_fit = check_if_fits(total_array, my_list[index])
            if not current_fit:
                return None
        return total_array,used
    else:
        for index,elem in enumerate(my_list):
            if(used[index] == False):
                if(check_if_valid(total_array, elem)):
                    used2 = list(used)
                    used2[index] = True
                    result = combine(total_array+elem,number-1,my_list,used2)
                    if result is not None:
                        return result                



f = open('B-small-attempt0 (1).in','r')
f2 = open('B-small-attempt0 (1).out','w')

numcases = int(f.readline())

for numcase in range(numcases):
    N = int(f.readline())
    papers = []
    for j in range(2*N-1):
        array = f.readline().split(" ")        
        papers.append([int(num) for num in array])
    result = combine([],N,papers,[False]*(2*N-1))   
    non_existing_columns = [True]*N
    not_used_indices = [index for index,e in enumerate(result[1]) if not e]
    for index in not_used_indices:
        for i in range(N):
            if(papers[index][0]==result[0][i]):
                non_existing_columns[i]= False
                break
    column = [i for i,c in enumerate(non_existing_columns) if c][0]
    final_result = []
    for i in range(N):
        final_result.append(str(result[0][(N*i) + column]))
    print(final_result)
    my_result = " ".join(final_result)
    f2.write("Case #{0}: {1}\n".format(numcase+1,my_result))
    
                