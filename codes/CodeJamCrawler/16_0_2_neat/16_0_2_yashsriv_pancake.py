def is_done(pos):
    if list(pos).count('+') == len(pos):
        return True
    return False

def flip(pos, i):
    new_pos = ''
    for j in range(len(pos)):
        if j + 1 <= i:
            if pos[j] == '+':
                new_pos += '-'
            else:
                new_pos += '+'
        else:
            new_pos += pos[j]
    return new_pos

def get_number_of_moves(node):
    Q = []
    Q.append(node)
    while len(Q) != 0:
        current = Q.pop()
        # print(current)
        if is_done(current[0]):
            return current[1]
        for i in range(1, len(current[0]) + 1):
            new_node = []
            new_node.append(flip(current[0], i))
            new_node.append(current[1] + 1)
            already = False
            for vals in Q:
                if new_node[0] == vals[0]:
                    already = True
            if not already:
                # print(new_node, i)
                # print('Q:', Q)
                # input()
                Q.insert(0, new_node)


if __name__ == '__main__':
    T = int(input())
    for case in range(1, T + 1):
        S = input()
        print('Case #%d: %d'% (case, get_number_of_moves([S, 0])))


