def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    array_cache = {}
    # I need to see if that number exists in another array
    # if it does return the values in a list in any order
    result = "wip"
    index = 0 
    for arr in arrays:
        print(arrays[index])
        if arr not in array_cache:
            array_cache[index] = index
        index += 1
    print(array_cache)

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
