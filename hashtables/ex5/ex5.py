# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    files_cache = {}
    for i in range(len(files)):
        if files[i] not in files_cache:
            file_key = files[i].split("/")
            files_cache[file_key[-1]] = files[i]
    for query in queries:
        if query in files_cache:
            result.append(files_cache[query])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
