def B(seq):
    previous = seq[0] if len(seq) else None
    maneuvers = 0
    for elem in seq:
        if elem != previous:
            maneuvers += 1
        previous = elem
    return maneuvers + (1 if previous == '-' else 0)
    