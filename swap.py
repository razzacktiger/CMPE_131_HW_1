list1 = [12,35,5,9,56,24]
def swap_last_item(list):
    """swap(list) takes in 1 argument of list value type 
       returns swaped last and first index of list
    """
    temp = list[-1]
    list[-1] = list[0]
    list[0] = temp 
    return list
