def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    num_cache = {}
    result = []
    # I need to see if that number exists in another array
    # if it does return the values in a list in any order
    for arr in arrays: # O(2^n best I could think o smh)
        for num in arr:
            print("num in arr", arr)
            if num not in num_cache:
                num_cache[num] = 0
            else:
                num_cache[num] += 1

    print(num_cache)

    return result


if __name__ == "__main__":
    arrays = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
    ]
    # arrays.append(list(range(10, 20)) + [1, 2, 3])
    # arrays.append(list(range(10, 20)) + [1, 2, 3])
    # arrays.append(list(range(10, 20)) + [1, 2, 3])
    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
