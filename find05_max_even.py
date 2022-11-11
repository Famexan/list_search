def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    max = data[0]
    for i in data:
        if i > max and i%2 == 0:
            max = i

    return max
