'''
Created on Mar 19, 2016

@author: elmoatasem
'''




# def excute_flip(string):
#     
#     for i in range(len(string)):
#         if(string[i] == '-'):
#             string[i] = '+'
#         else:    
#             string[i] = '-'
#             
#     return string[::-1]
# 
# 
# 
# def check_if_done(pattern_list):
#     done = True
#     for i in range(len(pattern_list)):
#         if(pattern_list[i] == '-'):
#             done = False
#     return done


def get_summarized_pattern(pattern_list):
    new_pattern = []
    last_val = ''
    for i in range(len(pattern_list)):
        if(pattern_list[i] <> last_val):
            new_pattern.append(pattern_list[i])
            last_val = pattern_list[i]
            
    return new_pattern
            
    
def get_min_manuvere_times(pattern):
    pattern_list = list(pattern)
    summarized_pattern =  get_summarized_pattern(pattern_list)
    if(summarized_pattern[0] == '-'):
        if(len(summarized_pattern) % 2 == 0):
            return len(summarized_pattern) - 1
        else:
            return len(summarized_pattern)
    else:
        if(len(summarized_pattern) % 2 == 0):
            return len(summarized_pattern)
        else:
            return len(summarized_pattern) - 1
    
    return 0







f_r = open('B-large.in',"r")
n_test=int(f_r.readline().strip()) 
f_w = open("B.out", "w")
result = ""
for i in range(n_test):
    pattern =  f_r.readline().strip()
#     print pattern[0]
#     print len(pattern)
    result = get_min_manuvere_times(pattern)
    print result
    output_str='Case #{itr}: {res}'.format(itr=(i+1),res=result)
    f_w.write(output_str+'\n')
    
f_r.close()



