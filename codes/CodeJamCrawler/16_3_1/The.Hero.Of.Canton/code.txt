import string

def solve(lst):
    alphabet = string.ascii_uppercase[:len(lst)]
    maxelem, maxidx1, maxidx2 = 0, -1, -1
    for idx, elem in enumerate(lst):
        if elem >= maxelem:
            maxelem = elem
            maxidx2 = maxidx1
            maxidx1 = int(idx)
        elif maxidx2 == -1 or elem >= lst[maxidx2]:
            maxidx2 = int(idx)
    
    
    evacuate = []
    
    diff = int(lst[maxidx1]) - int(lst[maxidx2])
    if diff > 0:
        evacuate.append(' '.join(diff * alphabet[maxidx1]))
    for idx, elem in enumerate(alphabet):
        if elem != alphabet[maxidx1] and elem != alphabet[maxidx2]:
            evacuate.append(' '.join(elem * int(lst[idx])))
    
    evac = alphabet[maxidx1] + alphabet[maxidx2] + ' '
    evacuate.append(''.join(evac * int(lst[maxidx2])))
    return ' '.join(evacuate)

# solve([2,4,3])