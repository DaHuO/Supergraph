
# coding: utf-8

# In[95]:

import time
# target = "prac"
target = "small"
# target = "large"
T = 0
problems = []
            


# In[96]:

with open(target + ".in") as f:
    T = int(f.readline())
    for line in range(T):
        problems.append(int(f.readline()))


# In[97]:

def sleep_number(N):
#     original_N = N
    target_N = N
    targets = [str(i) for i in range(10)]
    
    last_num = 0
    start_time = time.time()
    
    while len(targets) > 0:
#         print(targets)
        for cursor in [i for i in str(target_N)]:
#             print(cursor)
            if cursor in targets:
                targets.remove(cursor)
                last_num = target_N
        target_N += N
        
        elapsed_time = time.time() - start_time
        if elapsed_time > 10:
            return "INSOMNIA"
            break
        
    return last_num


# In[102]:

def print_result(L):
    with open(target + ".out","w") as f:
        for case_number, result in zip(range(1,len(L)+1), L):
            tmp = "Case#%d: %s\n"%(case_number, result)
            print(tmp)
            f.writelines(tmp)


# In[99]:

results = [sleep_number(i) for i in problems]
# print_result(result)


# In[100]:

results


# In[103]:

print_result(results)


# In[ ]:



