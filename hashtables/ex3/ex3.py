def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    array_cache = {}
    # I need to see if that number exists in another array
    # if it does return the values in a list in any order
    result = "wip"
    for arr in arrays:
        for num in arr:
            if num not in array_cache:
                array_cache[num] 

    return result


if __name__ == "__main__":
    arrays = []
    arrays.append(list(range(100, 200)) + [1, 2, 3])
    arrays.append(list(range(100, 200)) + [1, 2, 3])
    arrays.append(list(range(100, 200)) + [1, 2, 3])
    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
