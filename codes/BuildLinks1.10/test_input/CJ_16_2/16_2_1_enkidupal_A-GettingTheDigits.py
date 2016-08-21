
# coding: utf-8

# In[16]:

def load_testcases(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        t = int(lines[0])
        return (t, lines[1:])


# In[22]:

from collections import Counter
letter_map = {0: Counter('ZERO'), 1: Counter('ONE'), 2: Counter('TWO'), 3: Counter('THREE'), 4: Counter('FOUR'),
              5: Counter('FIVE'), 6: Counter('SIX'), 7: Counter('SEVEN'), 8: Counter('EIGHT'), 9: Counter('NINE')}
letter_list = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR',
              5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}


# In[44]:

def remove_digit_from_map(digit, letters_left):
    digit_str = letter_list[digit]
    for s in digit_str:
        letters_left[s] -= 1
    return letters_left


# In[55]:

def digit_removing_is_legal(digit, letters_left):
    digit_str = letter_list[digit]
    digit_counter = Counter(digit_str)
    for dd in digit_counter:
        if letters_left[dd] < digit_counter[dd]:
            return False   
    return True
        


# In[73]:

def get_next_moves(letters_left):
    ret = []
    for digit in range(0, 10):
        if digit_removing_is_legal(digit, letters_left):
            ret.append(digit)
    return ret


# In[75]:

def get_position_after_move(letters_left, move):
    ret = Counter(letters_left)
    remove_digit_from_map(move, ret)
    return ret
    


# In[30]:

def create_letter_list_from_word(word):
    return Counter(word)


# In[38]:

def letter_list_is_empty(letters_left):
    for digit in letters_left:
        if letters_left[digit] > 0:
            return False
    return True


# In[4]:

def write_solutions_to_file(out_fileName, testcases_solutions):
    with open(out_fileName, 'w') as f:
        t_len = len(testcases_solutions)
        for t in range(0, t_len):
            f.write('Case #' + str(t + 1) + ': ' + str(testcases_solutions[t]))
            if t != t_len-1:
                f.write('\n')


# In[112]:

def solve_testcase(testcase):
    letters_left  = create_letter_list_from_word(testcase)
    sol = sorted(solve_recursive([], letters_left))
    return ''.join(str(x) for x in sol)
    


# In[107]:

def solve_recursive(moves_so_far, letters_left):
    #print(moves_so_far, letters_left)
    if letter_list_is_empty(letters_left):
        return []
    candidate_moves = get_next_moves(letters_left)
    if len(candidate_moves) == 0:
        return None
    
    for cand_move in candidate_moves:
        rr = solve_recursive(moves_so_far + [cand_move], get_position_after_move(letters_left, cand_move))
        if rr is not None:
            return [cand_move] + rr
    return None
    


# In[81]:

def solve_all_testcases(testcases):
    t = testcases[0]
    vals = []
    for testcase in testcases[1]:
        vals.append(solve_testcase(testcase))
    return vals


# In[116]:

testcases = load_testcases('A-small-attempt0.in')
testcases_solutions = solve_all_testcases(testcases)

write_solutions_to_file('A-small-attempt0.out',testcases_solutions )

