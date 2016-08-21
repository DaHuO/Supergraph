def sheep_count(init):
    num_list = range(10)
    current = init
    step = 1
    if init == 0:
        return "INSOMNIA"
    while len(num_list) != 0:
        temp_current = step*init
        current = temp_current
        step += 1
        while temp_current >= 10:
            digit = (temp_current % 10)
            if digit in num_list:
                num_list.remove(digit)
            temp_current /= 10

        if temp_current < 10:
            if temp_current in num_list:
                num_list.remove(temp_current)

    return current 

inp = int(raw_input())
step = 1
while inp != 0:
    inp -= 1
    inp2 = int(raw_input())
    result = sheep_count(inp2)
    print ("Case #{}: {}".format(step, result))
    step += 1
