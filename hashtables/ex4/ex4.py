def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    negatives = [num for num in a if num < 0]
    # need to see if a negative has a positve counterpart
    # iterate through the list
    for num in a:
        # see if num is in cache
        if num not in cache and num >= 0:
            cache[num] = num
            # add it if not
    for num in negatives:
        num = -num
        if num in cache and num not in result:
            result.append(num)
    return result

result = has_negatives([-1,-2,1,2,3,4,-4])
result.sort()
print(result)


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
