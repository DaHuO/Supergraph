#!/usr/bin/python

dataset = open('B-small.in','r')
#dataset = open('AB-large.in','r')


def get_states(cakes):
    for i in range(len(cakes)):
        state = cakes[i:i+1]
        #print("digit is "+digit)
        states[i] = state
    #print("checked "+num)

def flip(states,num):
    for i in range(num+1):
        if states[i] == "+":
            states[i] = "-"
        else:
            states[i] = "+"

def check(states):
    if "-" not in states:
        return True

line_num = 0
for cakes in dataset:

    if(line_num==0):
        line_num+=1
    elif cakes == "\n":
        line_num+=1
    else:
        cakes = cakes.strip("\n")
        num_of_cakes = len(cakes)
        states = [0]*num_of_cakes
        get_states(cakes)

        if num_of_cakes == 1:
            if states[0] == "+":
                print("Case #"+str(line_num)+": 0")
            else:
                print("Case #"+str(line_num)+": 1")
            line_num+=1
        elif "-" not in states:
            print("Case #"+str(line_num)+": 0")
            line_num+=1
        elif "+" not in states:
            print("Case #"+str(line_num)+": 1")
            line_num+=1
        else:
            #print(states)
            is_finished = False
            flip_count = 0
            #prev = states[0]

            while not is_finished:
                #print(states)
                prev = states[0]
                for i in range(1,num_of_cakes):
                    cur = states[i]
                    if prev == cur:
                        prev = cur
                    else:
                        flipping_point = i
                        flipping_state = states[flipping_point]
                        prev = flipping_state
                        if flipping_point < num_of_cakes-1:
                            for j in range(flipping_point+1, num_of_cakes):
                                if states[j] == prev:
                                    prev = states[j]
                                    # modified part here
                                    if j == num_of_cakes-1:
                                        if cur == "+":
                                            flip(states,flipping_point-1)
                                            flip_count += 1
                                        else:
                                            flip(states,num_of_cakes-1)
                                            flip_count += 1
                                    # modified part end here
                                else:
                                    #print("flipping first "+str(j)+"cakes! for "+cakes)
                                    flip(states,j-1)
                                    flip_count += 1
                                    #print("DONE!",end="")
                                    #print(states)
                                    break
                        else:
                            if cur == "+":
                                flip(states,flipping_point-1)
                                flip_count += 1
                                #print(states)
                            else:
                                flip(states,num_of_cakes-1)
                                flip_count += 1
                                #print(states)
                        break
                #print("Check for ",end="")
                #print(states)
                if "+" not in states:
                    flip(states, num_of_cakes-1)
                    flip_count += 1
                is_finished = check(states)
                if is_finished:
                    print("Case #"+str(line_num)+": "+str(flip_count))

            line_num+=1