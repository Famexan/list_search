def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    max = data[0]
    for i in data:
        if i > max:
            max = i

    return data.index(max)
