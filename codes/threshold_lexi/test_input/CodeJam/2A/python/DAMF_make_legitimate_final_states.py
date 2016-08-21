

def down_one_round( players ):
    new_players = []
    for player in players:
        if player == "P":
            new_players.append("P")
            new_players.append("R")
        if player == "R":
            new_players.append("R")
            new_players.append("S")
        if player == "S":
            new_players.append("P")
            new_players.append("S")
    return "".join(new_players)

def rps_sort( answer ):
    #print("answer was " + answer)
    # The groups of 2 will always be sorted
    group_size = 4
    while group_size <= len(answer):
        # The group size is one in which we are going to sort the entities that are one size smaller
        new_answer = []
        for i in range(len(answer)/group_size):
            group_pieces = [answer[i*group_size:i*group_size + group_size/2],answer[i*group_size + group_size/2:(i+1)*group_size]]
            if group_pieces[1] < group_pieces[0]:
                temp = group_pieces[0]
                group_pieces[0] = group_pieces[1]
                group_pieces[1] = temp
            new_answer += group_pieces
            #new_answer.append(answer[i*group_size:(i+1)*group_size])
        #print("new answer was " + str(new_answer))
        answer = "".join(new_answer)
        group_size *= 2
    #print("answer is " + answer)
    return answer


for i in range(1,13):
    #print("Rounds: " + str(i))
    print("[")
    for start in ["P","R","S"]:
        answer = start
        for j in range(i):
            answer = down_one_round(answer)
        answer = rps_sort(answer)
        new_answer = [answer.count("P"), answer.count("R"), answer.count("S")]
        answer = new_answer
        print('\"' + str(answer) + '\",')
    print("],")

