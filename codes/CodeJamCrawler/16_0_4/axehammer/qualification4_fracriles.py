def solve(val_k, val_c, val_s):
    # CASE: If the number of tiles is 1
    if val_k == 1 and val_s >= 1:
        return [1] # 1 tile and more than 1 student should give the answer
    elif val_k == 1 and val_s == 0:
        return [-1] # Impossible as we've got no students to unviel the tile
    # CASE: Complexity is 1, ie: straight-forward
    if val_c == 1 and val_k <= val_s:
        return [(_ + 1) for _ in range(0, val_k)] # We've to go through all the tiles and we can as we've atleast the required number of students to do so
    elif val_c == 1 and val_k > val_s:
        return [-1] # We don't have enough students to go through the tiles
    # CASE: Complexity is more than one; preferable to go through all tiles within a certain range
    if val_s > val_k - 2:
        return [(_ + 2) for _ in range(0, val_k - 1)] # We've to go through all the tiles from the second on to one from the last
    else:
        return [-1] # Not possible

# Read the file
with open("qualification4_fracriles_input.txt", "r") as open_file, open("qualification4_fracriles_output.txt", "a+") as write_file:
    # Now, read the lines
    lines_of_file = [line.strip() for line in open_file.readlines()]
    # Now grab the number of test cases
    n = int(lines_of_file[0])
    # Iterate till n
    for _ in range(n):
        valK, valC, valS = [int(part) for part in lines_of_file[1+_].strip().split(" ")]
        result = solve(valK, valC, valS)
        # Print
        if result[0] == -1:
            print("CASE #" + str(1+_) + ":", "IMPOSSIBLE", file = write_file)
        else:
            print("CASE #" + str(1+_) + ":", ' '.join([str(val) for val in result]), file = write_file)
