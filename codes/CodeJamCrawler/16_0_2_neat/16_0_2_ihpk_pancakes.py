def pancakes(file_name):
    read_file_name = file_name
    write_file_name = file_name + ' - answer.txt'
    
    read_file = open(read_file_name)
    write_file = open(write_file_name, "w")
    
    cases = int(read_file.readline())
    
    current_case = 1
    
    while current_case <= cases:
        cakes = read_file.readline().rstrip("\n")
        cake_flips = find_num_flips(cakes)
        output = "Case #{0}: {1}\n".format(current_case, cake_flips)
        write_file.write(output)
        current_case += 1
        
def find_num_flips(cakes):
    
    i = 0
    while cakes != "+" * len(cakes):
        cakes = flip_cakes(cakes)
        i += 1
        
    return i

def flip_cakes(cakes):
    bottom_happy_side_up = len(cakes) - 1
    while cakes[bottom_happy_side_up] == "+":
        bottom_happy_side_up -= 1
        
    if cakes[0] == "-":
        cakes = flip_sides(cakes[0:bottom_happy_side_up + 1]) + cakes[bottom_happy_side_up + 1:]
        
        return cakes
    else:
        top_happy_side_up = 0
        while cakes[top_happy_side_up] == "+":
            top_happy_side_up += 1
        cakes = flip_sides(cakes[0:top_happy_side_up][::-1]) + cakes[top_happy_side_up:]
        return cakes
    
def flip_sides(cakes):
    flipped_cakes_wrong_side_up = cakes[::-1]
    flipped_cakes_right_side_up = ""
    for cake in flipped_cakes_wrong_side_up:
        if cake == "-":
            flipped_cakes_right_side_up += "+"
        else:
            flipped_cakes_right_side_up += "-"
    return flipped_cakes_right_side_up
    
if __name__ == "__main__":
    pancakes("test.in")
    pancakes("B-small-attempt1.in")
    pancakes("B-large.in")