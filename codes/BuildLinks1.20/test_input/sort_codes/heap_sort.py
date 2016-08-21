__author__ = 'rg.kavodkar'

from math import floor


def sort(list_):
    '''

    :param list_: a list of numbers for sorting
    :return: the sorted list
    '''
    length = len(list_)
    build_max_heap(list_, length)
    # The loop where the actual sorting is performed
    while length > 0:
        # The root will have the highest valued node of the unsorted list
        # Reduce the length of the unsorted list so that the sorted part remains untouched
        list_[length - 1], list_[0] = list_[0], list_[length - 1]
        length -= 1
        # Perform max-heapify to put the max valued element at the root
        max_heapify(list_, length)
    return list_


def max_heapify(list_, length):
    '''
    Perform the max heapify operation on the list which has the root swapped with the last node
    :param list_: The list of elements
    :param length: Length of the list yet unsorted
    :return: Returns a max after performing the sift-down operation
    '''
    index = 0
    while index < int(floor((length - 1)/2)):
        # Get the index of the maximum valued child and swap with that index
        max_child_index = get_max_child_index(list_, index, length)
        if list_[index] < list_[max_child_index]:
            list_[index], list_[max_child_index] = list_[max_child_index], list_[index]
            index = max_child_index
        else:
            break


def get_max_child_index(list_, index, length):
    '''

    :param list_: The list of elements
    :param index: The index whose children are to be inspected
    :param length: Length of the list yet unsorted
    :return: The index of the maximum valued child
    '''

    # The index of the left child
    left_child = 2*index + 1
    # The index of the right child
    right_child = 2*index + 2

    # If the left child index is less than the length of the unsorted list, return -1
    if left_child > length - 1:
        return -1
    # If the node just has one child, ie, the left child
    elif left_child == length - 1:
        return left_child

    # The code will reach this part only if the current node has 2 children
    # Check for whichever is higher valued and return the index
    if list_[left_child] > list_[right_child]:
        return left_child
    else:
        return right_child


def build_max_heap(list_, length):
    '''
    Build the max heap to get started with the sorting
    :param list_: The list of elements
    :param length: the length of the list yet unsorted
    :return: The list as a heap
    '''

    # Iterate through the list and perform the 'sift-up' operation
    for j in range(2, length):
        i = j
        while i > 0:
            parent_index = int(floor((i - 1)/2))
            if list_[i] > list_[parent_index]:
                list_[i], list_[parent_index] = list_[parent_index], list_[i]
                i = parent_index
            else:
                break