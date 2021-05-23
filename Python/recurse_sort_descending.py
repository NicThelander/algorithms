#  recursive descending sort for numeric lists
def recurse_sort_des(ls, active_index=0):
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
