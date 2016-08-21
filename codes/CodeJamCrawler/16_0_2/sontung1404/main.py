import sys
import random
import Queue


def flip_helper(seq):
    a_dict = {"+": 1, "-": 0}
    a_dict2 = {1: "+", 0: "-"}
    result = ""
    for i in range(len(seq)-1, -1, -1):
        result += a_dict2[int(not(a_dict[seq[i]]))]
    return result


def flip(seq, number):
    if number > len(seq):
        print "wrong input"
        return
    else:
        result = flip_helper(seq[:number]) + seq[number:]
        return result


def valid(seq):
    if "-" in seq:
        return False
    else:
        return True


def adj(node):
    result = []
    number = node.get_moves()
    seq = node.get_string()
    for _i in range(1, len(seq)+1):
        new_seq = flip(seq, _i)
        if new_seq != seq:
            new_node = Node(number+1, new_seq)
            result.append(new_node)
    return result


def examine(a_seq):
    if valid(a_seq):
        return 0
    a_queue = Queue.Queue()
    root = Node(0, a_seq)
    a_set_for_nodes = [root]
    a_set_for_seqs = [a_seq]
    a_queue.put(root)
    while not a_queue.empty():
        a_node = a_queue.get()
        for neighbor in adj(a_node):
            current_seq = neighbor.get_string()
            if valid(current_seq):
                return neighbor.get_moves()
            else:
                if current_seq not in a_set_for_seqs:
                    a_set_for_seqs.append(current_seq)
                    a_set_for_nodes.append(neighbor)
                    a_queue.put(neighbor)


class Node:
    def __init__(self, moves, a_string):
        self.moves = moves
        self.a_string = a_string

    def get_moves(self):
        return self.moves

    def get_string(self):
        return self.a_string


if __name__ == "__main__":
    sys.stdin = open("B-small-attempt0.in")
    sys.stdout = open("out.txt", "w")
    for case in range(1, int(sys.stdin.readline())+1):
        print "Case #%d: %d" % (case, examine(sys.stdin.readline()[:-1]))

    # char = ["+", "-"]
    # for case in range(100):
    #     seq = ""
    #     for i in range(10):
    #         seq += random.choice(char)
    #     print seq, examine(seq)




