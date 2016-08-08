from random import shuffle

def bogosort(seq):
    while(not all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1))):
        shuffle(seq)

    return seq