
def find_last_word(s):
    char_list = []
    for char in s:
        if len(char_list) == 0:
            char_list.append(char)
        elif char >= char_list[0]:
            char_list = [char] + char_list
        else:
            char_list.append(char)
    return ''.join(char_list)


if __name__ == '__main__':
    num_examples = int(input())
    for i in range(0, num_examples):
        s = input().strip()
        solution = find_last_word(s)
        print("Case #%s: %s" % (i+1, solution))
