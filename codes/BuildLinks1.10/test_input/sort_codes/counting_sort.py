__author__ = 'rg.kavodkar'


def sort(list_):
    '''
    Counting sort requires the range in which the numbers are distributed. Hence, we need to
    send the highest value in the list as the upper bound of the range
    This implementation is restricted to positive integers only
    :param list_: a list of numbers for sorting
    :return: the sorted list
    '''
    return counting_sort(list_, max(list_))


def counting_sort(list_, max_element):
    # A counter array that contain the number of occurrences of each element in the list
    counter = [None] * (max_element + 1)
    sorted_list = [None] * len(list_)

    # Initialize the counter array to 0
    for i in range(max_element + 1):
        counter[i] = 0

    # Initialize the counter array to 0
    for i in range(len(list_)):
        sorted_list[i] = 0

    # update the occurrences of each element in the counter array
    for i in range(len(list_)):
        counter[list_[i]] += 1

    # Add each counter to the previous one so that last position of the element is known
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]

    # The counter array will contain the last position of the given element, so that the
    # relative positions of the elements are not lost. Hence, starting from the end of
    # the original list, iterate in the reverse order and place them in their last position
    # and decrement so that the next element(in the reverse order) is placed at the right
    # position
    for i in reversed(range(1, len(list_))):
        sorted_list[counter[list_[i]] - 1] = list_[i]
        counter[list_[i]] -= 1
    return sorted_list