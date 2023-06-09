def last_element(lst):
    if len(lst) > 0:
        return lst[-1]
    return None
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

print(last_element([1, 2, 3]))
print(last_element([]))