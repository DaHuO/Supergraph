#insertion sort
import random

def insertion_sort(unsorted_list):
    num = len(unsorted_list)  ##get length of list
    for i in xrange(num-1):   ##iterate the list
        current = unsorted_list[i+1]  ##get current unsorted element
        position = i+1  ##get the position of current unsorted elment
        ##check whether a sorted element is greater than current unsorted element
        while position > 0 and unsorted_list[position-1] > current:
            unsorted_list[position] = unsorted_list[position-1]  ##shift sorted elments
            position = position -1
        unsorted_list[position] = current  ##insert current unsorted element


####test####
if __name__ == '__main__':
    unordered = random.sample(range(1,100),10) ##generate random samples
    print unordered
    insertion_sort(unordered)
    print unordered
