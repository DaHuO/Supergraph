def remove_word_from_list(l, w):
    w_l = list(w)
    for ll in w_l:
        l.remove(ll)
    return l

def phone_number(num_str):
    letters = list(num_str)
    numbers = []
    ordered_check = [0,2,4,6,8,1,3,5,7,9]
    char_map = {0:'Z', 2: 'W', 4: 'U', 6: 'X', 8: 'G', 1: 'O', 3: 'T', 5: 'F', 7: 'S', 9: 'E'}
    word_map = {0:'ZERO', 2: 'TWO', 4: 'FOUR', 6: 'SIX', 8: 'EIGHT', 1: 'ONE', 3: 'THREE', 5: 'FIVE', 7: 'SEVEN', 9: 'NINE'}
    for num in ordered_check:
        if char_map[num] in letters:
            for i in range(letters.count(char_map[num])):
                letters = remove_word_from_list(letters, word_map[num])
                numbers.append(num)
    numbers.sort()
    return ''.join(map(str,numbers))

        
def formatted_output(index, final_count):
    return 'Case #' + str(index) + ': ' + str(final_count)


t = int(raw_input())  
for i in range(1, t + 1):
    n= raw_input()
    print formatted_output(i, phone_number(n))