def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    # abs() turns a number to a positive
    # need to see if a negative has a positve counterpart
    # iterate through the list
    for i in range(len(a) - 1):
        # if the number is less than 0
        current_num = a[i]
        print(current_num)
        if current_num < 0:
            current_num = abs(current_num)
            # abs it
        # check if the number is in the cache
        if current_num not in cache:
            cache[i] = current_num
    print(cache)
    # result = [num for num in result if num ]
    return result

result = has_negatives([-1,-2,1,2,3,4,-4])
result.sort()
print(result)


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
