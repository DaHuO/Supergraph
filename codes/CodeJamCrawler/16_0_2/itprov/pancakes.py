#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import re

happy_sides_first_pattern = re.compile(r"^(\++)-+") # Pancakes starting with 1 or more +'s followed by at least 1 -
blank_sides_first_pattern = re.compile(r"^(-+)\++") # Pancakes starting with 1 or more -'s followed by at least 1 +

t = int(input()) # Number of test cases
for i in range(t):
    pancakes = input() # Given test case string
    j = 0 # Number of times of maneuvers
    while "-" in pancakes: # Repeat while at least 1 - exists
        match_found = happy_sides_first_pattern.match(pancakes) # Try first case - starting with +'s, e.g. ++--+-
        if match_found:
            matched_pancakes = match_found.group(1) # This is the first +'s that need to be flipped
            pancakes = pancakes.replace(matched_pancakes, "-" * len(matched_pancakes), 1)
        elif blank_sides_first_pattern.match(pancakes): # Try second case - starting with -'s, e.g. ---++-+
            match_found = blank_sides_first_pattern.match(pancakes)
            matched_pancakes = match_found.group(1) # This is the first -'s that need to be flipped
            pancakes = pancakes.replace(matched_pancakes, "+" * len(matched_pancakes), 1)
        else: # This last case means all pancakes are -'s
            pancakes = pancakes.replace("-", "+")
        j = j + 1
    print("Case #{}: {}".format(i + 1, j))
