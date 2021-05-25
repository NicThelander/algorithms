def recurse_sort_des(ls, active_index=0):
    """
    Passed a list as an argument and then recursively
    finds and swaps the biggest integer from further in
    the list with the current position.

    Note: The active index is used for tracking it's place
    within the list, you can supply one yourself but it will
    only process from that index onwards then.

    :param ls: The list that should be passed to the function
    :param active_index: To keep track of the index position
    being worked on, you can supply your own one to declare
    where in the list it should start.
    :return: Returns the sorted list from biggest to smallest
    """
    swap_val = ls[active_index]
    swap_index = active_index
    if len(ls) - 1 > active_index:
        for i in range(active_index + 1, len(ls)):
            if ls[i] > swap_val:
                swap_val = ls[i]
                swap_index = i
        temp_val_holder = ls[active_index]
        ls[active_index] = swap_val
        ls[swap_index] = temp_val_holder
        active_index += 1
        return recurse_sort_des(ls, active_index)
    else:
        return ls
