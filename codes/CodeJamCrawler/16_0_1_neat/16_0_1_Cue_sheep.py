import numpy as np

filename = 'A-large.in'
out_filename = 'large_out_data.dat'

out_file = open(out_filename,'w')
raw_data = np.loadtxt(filename,dtype=np.int32)

count = raw_data[0]
data = raw_data[1:]

def _num_to_bool(val):
    '''takes a number and converts to a boolean_array
    '''
    #TODO Could speed this up
    characters_bool = np.zeros(10,dtype=bool)
    indeces = map(int,list(str(val)))
    for index in indeces:
        characters_bool[index] = True
    return characters_bool

def _check_num(characters_bool,val):
    '''Take a number and updates the character_bool
    '''
    new_characters_bool = _num_to_bool(val)
    out_characters_bool = new_characters_bool + characters_bool
    return out_characters_bool

def analyse(start_N):
    '''Analyses a number from the input
    '''
    if int(start_N) is 0:
        return 'INSOMNIA'
    characters_bool = np.zeros(10,dtype=bool)
    multiplier = 1
    while not characters_bool.all():
        cur_N = start_N*multiplier
        print cur_N
        characters_bool = _check_num(characters_bool,cur_N)
        multiplier += 1
    sleep_N = cur_N  
    return sleep_N

def write_output(out_file,N_list):
    case_int = 1
    for N in N_list:
        out_file.write('Case #{0}: {1}\n'.format(case_int,N))
        case_int += 1

N_list = []
for N in data:
    sleep_N = analyse(N)
    N_list.append(sleep_N)


write_output(out_file,N_list)
out_file.close()
