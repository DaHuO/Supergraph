__author__ = 'rg.kavodkar'

'''
Not implemented. DO NO USE!.
'''


def sort(list_):
    merge_sort(list_, 0, len(list_) - 1)


def merge_sort(list_, left, right):
    '''
    Split the list recursively until it reach unit size and retract from that point by merging the
    already sorted unit list, and so on.
    This performs the merge sort without taking any extra space
    :param list_: a list of numbers for sorting
    :return: the sorted list
    '''

    # In the recursive calls, if the size of the list is 1, return it
    if len(list_) == 1:
        return list_

    # Find the mid point of the list for splitting
    mid_point = int((left + right)/2)

    # The left and right halves of the list
    merge_sort(list_, left, mid_point)
    merge_sort(list_, mid_point + 1, right)

    # Merge the two sorted lists
    merge(list_, left, mid_point, right)
    return list_


def merge(list_, left, mid_point, right):
    '''
    Given two sorted list, merge them to form a unified sorted list
    :param list_1: Sorted list 1
    :param list_2: Sorted list 2
    :return: Returns the merged sorted list
    '''

    # an empty list to construct the sorted list
    # 2 moving pointers for the 2 lists
    l = left
    r = mid_point + 1

    # Starting from the head of both of the lists, add the smaller value to the sorted list
    # and move the corresponding pointer. Repeat until either of the pointers move out of scope
    while l <= mid_point and r <= right:
        if list_1[l] < list_2[r]:
            merged_list.append(list_1[l])
            l += 1
        else:
            merged_list.append(list_2[r])
            r += 1

    # For the pointer that dint move till the end, add the rest of the values in that list
    # to the sorted list
    if l < len(list_1):
        while l < len(list_1):
            merged_list.append(list_1[l])
            l += 1
    elif r < len(list_2):
        while r < len(list_2):
            merged_list.append(list_2[r])
            r += 1

