
# coding: utf-8

# In[123]:

import itertools
def pancake(cake_face):
    counter = 0
    face_list = list(cake_face)
    if "-" not in face_list:
        return counter
    elif all_equal(face_list):
        return counter+1
    else:
        index = 1
        while "-" in face_list:
            if face_list[index-1] != face_list[index]:
                temp_change = list(map(change, face_list[:index]))
                counter += 1
                face_list = temp_change + face_list[index:]
            index += 1
            if all_equal(face_list) and "-" in face_list:
                face_list = list(map(change, face_list))
                counter += 1
        return counter
    
def change(x):
    if x == "-":
        return "+"
    else:
        return "-"


def all_equal(facelist):
    "Returns True if all the elements are equal to each other"
    g = itertools.groupby(facelist)
    return next(g, True) and not next(g, False)

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = input()  # read a list of integers, 2 in this case
    print("Case #{}: {}".format(i, pancake(n)))

