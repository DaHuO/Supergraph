import fileinput
import copy

def is_good_addition(score_board, lst, start_coord, direction):
    #print ">>>>>>In is_good"
    #print score_board
    #print lst,start_coord,direction
    value = 1
    if start_coord >= len(score_board):
        #print "Bailing out, start is:",start_coord
        return False
    for i,v in enumerate(lst):
        #print i,start_coord,v
        if direction:
            if score_board[i][start_coord] != v and score_board[i][start_coord] != 0:
                #print "<<<<<Bad1"
                return False
            for j in range(len(score_board)):
                if score_board[j][start_coord] == v and j != i:
                    #print "<<<< Bad4"
                    return False
                if score_board[i][j] == v and j != start_coord:
                    #print "<<<< Bad5"
                    return False
            if score_board[i][start_coord] != 0:
                value += 1
        else:
            if score_board[start_coord][i] != v and score_board[start_coord][i] != 0:
                #print "<<<<Bad2"
                return False
            for j in range(len(score_board)):
                if score_board[start_coord][j] == v and j != i:
                    #print "<<<< Bad4"
                    return False
                if score_board[j][i] == v and j != start_coord:
                    #print "<<<< Bad5"
                    return False
            if score_board[start_coord][i] != 0:
                value += 1
    #print "<<<<<<Good"
    return value

def generate_good_addition(score_board, lst, start_coord, direction):
    score_board = copy.deepcopy(score_board)
    for i,v in enumerate(lst):
        if direction:
            score_board[i][start_coord] = v
        else:
            score_board[start_coord][i] = v
    return score_board


def step_down(scored_board,remaining_items,posted_lists,wildcard_used):
    #print "======In step_down, scores:",posted_lists,wildcard_used
    if len(remaining_items) == 0:
        return scored_board
    l = remaining_items[0]
    for d in [True,False]:
        val = is_good_addition(scored_board,l,posted_lists[d],d)
        if val:
            new_list = copy.deepcopy(posted_lists)
            new_list[d] += 1
            res = step_down(generate_good_addition(scored_board,l,posted_lists[d],d),
                            remaining_items[1:],new_list,wildcard_used)
            if len(res) != 0:
                return res
    if not wildcard_used:
        for d in [True, False]:
            new_list = copy.deepcopy(posted_lists)
            new_list[d] += 1
            if new_list[d] > len(scored_board):
                #print "Skipping wildcard",d
                continue
            res = step_down(scored_board,
                            remaining_items,new_list,True)
            if len(res) != 0:
                return res
    #print "====1111 Out step_down, scores:",posted_lists,wildcard_used
    return []
        

def align_lists(possible_lists,test_dir,skip_first):
    #Algorithm: Find the list that starts with the smallest number
    # There should be 2 lists starting with this number. They are the leftmost and topmost rows (arbitrary selection between these 2)
    # If no 2 lists start with same number, one of the edge rows is the missing list, we will rebuild it momentarily
    # Assuming we found both lists
    # Go down one of the lists. For each element there, try to select a list that matches it f
    sorted_lists = sorted(possible_lists)
    #print sorted_lists
    score_board = [list([0]*len(sorted_lists[0])) for x in range(len(sorted_lists[0]))]
    return step_down(score_board,sorted_lists,[0,0],False)

def gen_lines(board):
    collect = []
    for x in range(len(board)):
        collect.append([board[x][y] for y in range(len(board))])
        collect.append([board[y][x] for y in range(len(board))])
    return collect

def main():
    it = fileinput.input()
    num_cases = int(it.next())
    for i in range(1,num_cases+1):
        size = int(it.next())
        collect = []
        for n in range(2*size-1):
            collect.append([int(x) for x in it.next().split()])
        full = align_lists(collect,0,False)
#        print full
#        if len(full) == 0:
#            full = align_lists(collect,1,False)
#        if len(full) == 0:
#            full = align_lists(collect,0,True)
        assert len(full) > 0
        full = sorted(gen_lines(full))
        collect = sorted(collect)
        collect.append(None)
        for x,y in zip(full,collect):
            if x != y:
                print "Case #%d: %s" % (i," ".join(str(v) for v in x))
                break
        

if __name__ == "__main__":
    main()
